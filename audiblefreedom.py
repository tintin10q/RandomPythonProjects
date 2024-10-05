#!/bin/python
"""Note that this project does NOT 'crack' the DRM.
It simply allows the user to use their own encryption key (fetched from Audible servers) to decrypt the audiobook in the same manner that the official audiobook playing software does.
Please only use this application for gaining full access to your own audiobooks for archiving/conversion/convenience.
DeDRMed audiobooks should not be uploaded to open servers, torrents, or other methods of mass distribution.
No help will be given to people doing such things.
Authors, retailers, and publishers all need to make a living, so that they can continue to produce audiobooks for us to hear, and enjoy.
"""

import dataclasses
import io
import json
import os
import re

import shutil
import subprocess

import sys
from pathlib import Path
from typing import List, Protocol, cast

from multiprocessing import Pool

from argparse import ArgumentParser, FileType

parser = ArgumentParser(
    prog='audiblefreedom',
    description='Convert audible .aax files into playable audio like mp3 and split it into chapters')

parser.add_argument('filename', help="Your .aax file (downloaded from audible)")  # positional argument
parser.add_argument('--no-chapters', default=False, action='store_true', help="Do not generate chapters and only generate one large audio file")  # option that takes a value
parser.add_argument('-q', '--quiet', default=False, action='store_true', help="Do not log information, only errors and prompts. Disable prompts with --no-recreate")
parser.add_argument('-y', '--recreate', default=False, action='store_true', help="Generate files again even if they seem to be already generated (based on filename).")
group = parser.add_mutually_exclusive_group()
group.add_argument("--bytes-file", default="bytes.txt", help="Path to bytes.txt file.")
group.add_argument("--bytes", help="Pass your bytes as an argument", type=str)


class Args(Protocol):
    bytes: str
    bytes_file: str
    filename: str
    no_chapters: bool
    quiet: bool
    recreate: bool


args: Args = parser.parse_args()  # 'bytes', 'bytes_file', 'filename', 'no_chapters', 'quiet', 'recreate'


def log(*print_arg, **print_kwargs):
    if not args.quiet:
        print(*print_arg, **print_kwargs)

def error(*print_arg, **print_kwargs):
    print(*print_arg, **print_kwargs, file=sys.stderr)


input_path = Path(args.filename)
if not input_path.is_file():
    error("File not found:", input_path, file=sys.stderr)
    exit()

path_m4a = input_path.with_suffix(".m4a")

# Could use snowcrypt but we need ffmpeg anyway to create the chapters
if not shutil.which("ffmpeg") or not shutil.which("lame") or not shutil.which("mkvmerge"):
    error("Required program is missing! I cannot continue", file=sys.stderr)
    error("Run the following command(s) to install all required programs", file=sys.stderr)
    error("sudo apt install mkvtoolnix ffmpeg lame", file=sys.stderr)
    exit(1)

if args.bytes:
    activation_bytes = args.bytes
else:
    if not os.path.exists(args.bytes_file):
        error("Activation bytes file (bytes.txt) is missing! Please use")
        error("audible-cli (https://github.com/mkb79/audible-cli) or audible-activator (https://github.com/inAudible-NG/audible-activator/)")
        error("to get your activation bytes and save them to a file called bytes.txt in my working directory which is:")
        error(os.getcwd())

    with open(args.bytes_file, "r") as bytes_file_o:
        activation_bytes = bytes_file_o.read().strip()
print(activation_bytes)
code = os.system(f"ffmpeg -stats -loglevel 16 -activation_bytes {activation_bytes} -i {input_path} {'-y' if args.recreate else '-n'} -vn -c:a copy {path_m4a}")

if not ():
    log("Stripped DRM...")
elif code == 256:
    log(f"Got ffmpeg code 256 which means file with name '{path_m4a}' already exists. Moving on...")
else:
    error("Something went wrong with ffmpeg, got non zero exit code:", code, file=sys.stderr)
    # Here we could fallback on snowcrypt

log(f"Generated file: {path_m4a}")
if args.no_chapters:
    log("Not generating chapters")
    exit()

book_data = subprocess.run(["ffprobe", "-v", "quiet", "-show_format", "-print_format", "json", path_m4a], stdout=subprocess.PIPE)
book_data = json.loads(book_data.stdout)

match book_data:
    case {"format": {"tags": {"title": str(title), "artist": str(artist), "copyright": str(copyright), "album_artist": str(album_artist), "album": str(album), "date": str(date), "comment": str(comment), "genre": str(genre)}}}:
        pass
    case {"format": {"tags": {"title": str(title), "artist": str(artist)}}}:
        genre = "Audiobook"
        album_artist = artist
        album = title
        comment = ""
        copyright = ""
        date = ""
    case _:
        error("Could not read metadata! Got:", book_data)
        error("Could not read metadata, change the script if this happens too often.")
        exit(1)


def adjust_book_title(book_title, author):
    token_words = ["A", "An", "The"]
    fs_book_title = book_title.strip()
    fs_author = author.strip()

    for token in token_words:
        if fs_book_title.startswith(f"{token} "):
            # Remove the token from the beginning of the title
            fs_book_title = re.sub(f"^{token} ", "", fs_book_title)

            # If the book has a subtitle, move the token word before it
            if ": " in fs_book_title:
                fs_book_title = re.sub(r": ", f", {token}: ", fs_book_title)
                break

            # If no subtitle, append the token word to the end
            fs_book_title = f"{fs_book_title}, {token}"
            break
    # Replace invalid characters in the book title
    fs_book_title = re.sub(r'[<>"/\\|?*]', '-', fs_book_title)
    fs_book_title = re.sub(r': ', ' - ', fs_book_title)
    fs_book_title = re.sub(r':', ' - ', fs_book_title)

    # Replace invalid characters in the author name
    fs_author = re.sub(r'[<>"/\\|?*]', '-', fs_author)
    fs_author = re.sub(r': ', ' - ', fs_author)
    fs_author = re.sub(r':', ' - ', fs_author)
    return fs_book_title, fs_author


fs_book_title, fs_author = adjust_book_title(title, artist)


@dataclasses.dataclass
class Chapter:
    start: float
    end: float
    title: str
    index: int


def get_chapters(file_path: str) -> List[Chapter]:
    cmd = [
        'ffprobe', '-i', file_path, '-print_format', 'json', '-show_chapters', '-loglevel', 'error',
    ]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    chapters_info = json.loads(result.stdout)

    chapters = []
    for index, chapter in enumerate(chapters_info['chapters']):
        start_time = float(chapter['start_time'])
        end_time = float(chapter['end_time'])
        title = chapter.get('tags', {}).get('title', f"Chapter_{len(chapters) + 1}")
        chapters.append(Chapter(start_time, end_time, title, index + 1))

    return chapters


if not os.path.exists(fs_book_title):
    os.makedirs(fs_book_title)

chapter_output_suffix = ".mp3"


def encode_chapter(chapter: Chapter):
    output_file = Path(fs_book_title) / f"{chapter.title}.m4a"
    cmd = [
        'ffmpeg', '-i', f"{path_m4a}", '-ss', str(chapter.start), '-to', str(chapter.end),
        '-loglevel', 'error',
        "-c", "copy",
        output_file,
        ('-y' if args.recreate else '-n')
    ]

    log(f"Extracting chapter {chapter.index} from the large file")
    # print("by running command:", "".join([str(f'"{c}"') if not isinstance(c, str) else c for c in cmd])
    subprocess.run(cmd)

    output_file_mp3 = Path(fs_book_title) / f"{chapter.title}{chapter_output_suffix}"

    cmd2 = [
        "ffmpeg", "-i", f"{output_file}",
        '-loglevel', 'error',
        '-metadata', f'album={title}',
        '-metadata', f'genre={genre}',
        '-metadata', f'title={title} - {chapter.title}',
        '-metadata', f'artist={artist}',
        '-metadata', f'album_artist={album_artist}',
        '-metadata', f'date={date}',
        '-metadata', f'comment={comment}',
        '-metadata', f'track={chapter.index}/{len(chapters)}',
        '-id3v2_version', '3',
        '-codec:a', 'libmp3lame',
        '-qscale:a', '2',
        output_file_mp3,
        ('-y' if args.recreate else '-n')
    ]
    log(f"Starting to encode chapter {chapter.title} into mp3")
    # print("Running command:", " ".join([str(f'"{c}"') if not isinstance(c, str) else c for c in cmd2]))
    subprocess.run(cmd2)

    rm_cmd = ["rm", output_file]
    log(f"Removing m4a file for chapter {chapter.index}")
    subprocess.run(rm_cmd)
    # print("by running:", " ".join([str(f'"{c}"') if not isinstance(c, str) else c for c in cmd2]))


chapters = get_chapters(str(path_m4a))

with Pool(max(1, os.cpu_count() - 2)) as pool:
    for index, _ in enumerate(pool.imap(encode_chapter, chapters)):
        log(f"Encoded chapter number {index}")

"""
for chapter in chapters:
    p = Path(fs_book_title) / chapter.title
    p = p.with_suffix(".mp3")
    print(p, p.exists())
"""

log("Removing large m4a file for chapters!")

os.remove(path_m4a)

log("This keyboard error is not an error!")
raise KeyboardInterrupt(r"Not an error, but my shell breaks if I don't do this ¯\_(ツ)_/")
