PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as names_list:
    names = names_list.readlines()

with open("./Input/Letters/starting_letter.txt") as template:
    contents = template.read()
    for name in names:
        stripped_name = name.strip("\n")
        output = contents.replace(PLACEHOLDER, stripped_name)
        path = f"./Output/ReadyToSend/{stripped_name}.txt"
        with open(path, mode="w") as outfile:
            outfile.write(output)

    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp