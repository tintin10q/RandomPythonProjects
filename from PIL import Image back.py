from PIL import Image
from string import printable
image = Image.open("difference.png")
image2 = Image.open("difference2.png")
image_out = list(image.getdata())
image_out2 = list(image2.getdata())

boom1 = [i[1] for i in image_out]
boom2 = [i[1] for i in image_out2]
awsner = []
number = 0
for i in boom1:
    if boom2[number] - boom1[number] > 0:
        awsner.append(boom2[number] - boom1[number])
    number+=1

to_num_dict = {}
to_str_dict = {}
character_id =1
for character in "ABCDEFGHIJKLMNOPQRSTUVWXYZ".lower():
    to_num_dict[character] = character_id
    to_str_dict[character_id] = character
    character_id += 1

output = []
for i in awsner:
    output.append(to_str_dict[i])
print("".join(output))
