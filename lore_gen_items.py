from re import sub
import json
lore_data = json.load(open("item_lore_data.json","r"))

for lore in lore_data:
    if lore["ability"] != "":
        print_string = r'give @s minecraft:carrot_on_a_stick{display:{Name:"{\"text\":\"VVV\",\"color\":\"yellow\",\"italic\":false}",Lore:["{\"text\":\"ABILITY_text1\",\"color\":\"green\",\"italic\":false}"]},TAG_text} 1'
    if lore["ability2"] != "":
        print_string = r'give @s minecraft:carrot_on_a_stick{display:{Name:"{\"text\":\"VVV\",\"color\":\"yellow\",\"italic\":false}",Lore:["{\"text\":\"ABILITY_text1\",\"color\":\"green\",\"italic\":false}","{\"text\":\"ABILITY_text2\",\"color\":\"green\",\"italic\":false}"]},TAG_text} 1'
    if lore["ability3"] != "":
        print_string = r'give @s minecraft:carrot_on_a_stick{display:{Name:"{\"text\":\"VVV\",\"color\":\"yellow\",\"italic\":false}",Lore:["{\"text\":\"ABILITY_text1\",\"color\":\"green\",\"italic\":false}","{\"text\":\"ABILITY_text2\",\"color\":\"green\",\"italic\":false}","{\"text\":\"ABILITY_text3\",\"color\":\"green\",\"italic\":false}"]},TAG_text} 1'
    if lore["ability4"] != "":
        print_string = r'give @s minecraft:carrot_on_a_stick{display:{Name:"{\"text\":\"VVV\",\"color\":\"yellow\",\"italic\":false}",Lore:["{\"text\":\"ABILITY_text1\",\"color\":\"green\",\"italic\":false}","{\"text\":\"ABILITY_text2\",\"color\":\"green\",\"italic\":false}","{\"text\":\"ABILITY_text3\",\"color\":\"green\",\"italic\":false}","{\"text\":\"ABILITY_text4\",\"color\":\"green\",\"italic\":false}"]},TAG_text} 1'

    print_string = sub("VVV",str(lore["name"]),print_string)
    # print_string = sub("XXX",str(lore["mobility"]),print_string)
    # print_string = sub("YYY",str(lore["attack"]),print_string)
    # print_string = sub("ZZZ",str(lore["health"]),print_string)
    print_string = sub("ABILITY_text1",str(lore["ability"]),print_string)
    print_string = sub("ABILITY_text2",str(lore["ability2"]),print_string)
    print_string = sub("ABILITY_text3",str(lore["ability3"]),print_string)
    print_string = sub("ABILITY_text4",str(lore["ability4"]),print_string)
    print_string = sub("TAG_text",str(lore["tags"]),print_string)

    print(print_string)