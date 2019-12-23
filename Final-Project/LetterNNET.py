from random import randrange
import ast
class LetterNNET:
    def __init__(self):
        self.T_1H = [None] * 8
        self.T_2H = [None] * 8
        self.T_3H = [None] * 8
        self.T_4H = [None] * 8

        self.T_1L = [None] * 8
        self.T_2L = [None] * 8
        self.T_3L = [None] * 8
        self.T_4L = [None] * 8

        self.H = [[1,0,1,1,1,1,1,0,1,1,0,1],[1,0,1,1,0,1,1,1,1,1,0,1],[1,0,1,1,1,1,1,1,1,1,0,1]]
        self.L = [1,0,0,1,0,0,1,0,0,1,1,1]
    def grabData(self, file_name):
        read_file = open(file_name,"r")
        line_read = read_file.readlines()
        new_list = [[]]
        for line in line_read:
            new_list.append(list.copy(ast.literal_eval(line)))
        return new_list
    def generateHData(self,file_name, dataSize):
        current_file = open(file_name,"w")
        for i in range(0, dataSize):
            rand_H_copy = randrange(0,3) # Picking a random H template to use
            new_H = list.copy(self.H[rand_H_copy]) # Making a copy of the H template
            pixel_noise = randrange(0,12) # Picking the random noise pixel
            new_H[pixel_noise] = 1-new_H[pixel_noise] # Negating the pixel value at the noise index
            print(new_H,file=current_file)
        current_file.close()
    def generateLData(self,file_name, dataSize):
        current_file = open(file_name,"w")
        for i in range(0, dataSize):
            new_H = list.copy(self.L) # Making a copy of the L template
            pixel_noise = randrange(0,12) # Picking the random noise pixel
            new_H[pixel_noise] = 1-new_H[pixel_noise] # Negating the pixel value at the noise index
            print(new_H,file=current_file)
        current_file.close()

    def sampleTesting(self,sample_data_fname):
        pass
    def trainHSet(self, data_fname):
        data_lists = self.grabData(data_fname)
    def trainLSet(self, data_fname):
        data_lists = self.grabData(data_fname)