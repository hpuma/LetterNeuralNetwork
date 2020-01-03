from LetterNNET import LetterNNET
test = LetterNNET()

noise = 1
sampling_size = 3

# training_size = 200
# sample_size = 200
# test.generateHData("H_Training_set.txt",training_size, noise)
# test.generateLData("L_Training_set.txt",training_size, noise)
# test.generateSample("test_data.txt",sample_size, noise)
j_set = [0,4,8,1,3,7,2,5,6,9,10,11]
j_set1 = [[0,4,8],[1,3,7],[2,5,6],[9,10,11]]
test.trainHSet("H_Training_set.txt",sampling_size,j_set1)
test.trainLSet("L_Training_set.txt",sampling_size,j_set1)
test.sampleTesting("test_data.txt",sampling_size)    
print("SUCCESS??!!")