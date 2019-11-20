# Exercise
# Make a list for each line of a file, where each element of a list is a word
# of the text file.
current_file = open("ListFile.txt","w") # Name and location of the output file
list_print = ["This","is","an","arbitrary","list", "that","is","being","printed","on","a","file."] # List containing words to be printed on the file
[print(i,file=current_file,end="\n") for i in list_print]  # Iterates through entire list and adds it to the file
current_file.close()