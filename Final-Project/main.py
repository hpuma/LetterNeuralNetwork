from LetterNNET import LetterNNET
test = LetterNNET()
# test.generateHData("H_Training_set.txt",200,1)
# test.generateLData("L_Training_set.txt",200,1)
test.trainHSet("H_Training_set.txt",1)
test.trainLSet("L_Training_set.txt",1)
test.sampleTesting("test_data.txt",3)    
print("SUCCESS??!!")