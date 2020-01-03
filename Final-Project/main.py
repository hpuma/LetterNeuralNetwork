from LetterNNET import LetterNNET
test = LetterNNET()

noise = 1
sampling_size = 3

# training_size = 100
# sample_size = 1000
# test.generateHData("H_Training_set.txt",training_size, noise)
# test.generateLData("L_Training_set.txt",training_size, noise)
# test.generateSample("test_data.txt",sample_size, noise)

test.trainHSet("H_Training_set.txt",sampling_size)
test.trainLSet("L_Training_set.txt",sampling_size)
test.sampleTesting("test_data.txt",sampling_size)    
print("SUCCESS??!!")