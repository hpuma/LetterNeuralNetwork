from LetterNNET import LetterNNET

test = LetterNNET()
test.generateHData("H_Training_set.txt",50)
test.grabData("H_Training_set.txt")
test.generateLData("L_Training_set.txt",50)
print("SUCCESS??!!")