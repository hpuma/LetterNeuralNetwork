from LetterNNET import LetterNNET
test = LetterNNET()
test.trainLSet("L_Training_set.txt")

test_list = test.randomTuple(24,3)
print(test_list)    

print("SUCCESS??!!")
