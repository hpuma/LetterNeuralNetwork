from LetterNNET import LetterNNET
test = LetterNNET()

noise = 1
sampling_size = 3 # Sizes of the tuples. Changing this may cause instability

# Generating the training sets and the sample data. We do not need this since it has already been generated
# NOTE: uncomment lines 9 - 13 if you want new training set or sample tests
# training_size = 200 # Size both the training sets used to train the neural network
# sample_size = 200 # Size of the sample_data that will be used to test the neural network
# test.generateHData("H_Training_set.txt", training_size, noise) # Generates the H training and outputs to a file
# test.generateLData("L_Training_set.txt", training_size, noise) # Generates the L training and outputs to a file
# test.generateSample("test_data.txt", sample_size, noise) # Generates the sample usedto test the neural network

# Custom J sets that are used for sampling
j_set = [[0,4,8],[1,3,7],[2,5,6],[9,10,11]]
# Training the sets and test the neural network with the sample data
test.trainHSet("H_Training_set.txt", sampling_size, j_set)
test.trainLSet("L_Training_set.txt", sampling_size, j_set)
test.sampleTesting("Test_data_set.txt", sampling_size)