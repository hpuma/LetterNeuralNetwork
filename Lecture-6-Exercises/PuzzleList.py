# Look through a file of words, one word per line, and identify any English
# word that has all the vowels in order, with only one example of each
# vowel.
# For example, “abstemious”, “facetious”, “abstentious”
read_file = open("ReadMe.txt","r") # File to be read 
out_file = open("ReadMeResults.txt","w+") # Output file where each line represents a boolean on whether or not the word has the vowels in order
vowels = ["a","e","i","o","u"] # Vowel list used for comparing each line
lineread = read_file.readlines(); # List containing each line of the input file where each line is stored as a string

for line in lineread: # Iterating through the lines that were in the input file
    line = line.lower() # Making all the chars in a line to lower case so that we can easily compare with the vowels list
    index = 0 # Setting the index pointer back to the beginning of the list
    for i in line: # Iterating through all the chars in the string 
        if(i == vowels[index]): # Compare the string chars with the current vowel, if it matches then move the index pointer to compare with the next vowel
            index += 1
        if index == 5: # If we have found all the vowels, then print True to the output file and stop checking chars in line
            print("True",end="\n",file=out_file)
            break
    if(index < 5): # If we have iterated throughout the entire string and we haven't found all the vowels, the print false to the output file
        print("False",end="\n",file=out_file)
# Closing files
read_file.close()
out_file.close()