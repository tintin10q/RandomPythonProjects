from PIL import Image
from string import printable
image = Image.open("difference.png")
image_out = Image.new(image.mode,image.size)

to_num_dict = {}
to_str_dict = {}
character_id =1
for character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower():
    to_num_dict[character] = character_id
    to_str_dict[character_id] = character
    character_id += 1
message= "hallodaarhoegaathetmetje"
output = []
for i in message.lower():
    output.append(to_num_dict[i])


pixels = list(image.getdata())
print(pixels[:len(message)],"\n")
pixels = [list(i) for i in pixels]


id = 0
for i in output:
    pixels[id][1] += i
    id += 1



pixels = [tuple(i) for i in pixels]

print(pixels[:len(message)],"\n")

image_out.putdata(pixels)
image_out.save('difference2.png')
image = Image.open("difference2.png")
pixelscheck = list(image.getdata())
print(pixelscheck[:50])

if pixelscheck != pixels:
    print("It did not work use png istead compression forked up")

