is_list = False
new_text = ""
print(new_text)
text = open("input.txt","r+").readlines()
for i in text:
    if "â€¢" in i:
        if is_list == False:
            i = "<ul>\n<li>" + i
            is_list = True
        else:
            i = "<li>" +i
        i = i[:len(i)-1] + "</li>\n"
        new_text += i
    else:
        if is_list:
            i = "</ul>\n" + i
            is_list = False
        new_text += i
new_text.replace("•	","")
open("output_file.txt","w+").write(new_text)
print("Done! Added <li></li> and <ul></ul>")
        
