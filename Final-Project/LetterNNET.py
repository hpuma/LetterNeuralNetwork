from random import randrange
import ast
class LetterNNET:
    def __init__(self):
        # Top -> Bottom 0,1,2,3
        # H counts 
        self.T_H = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
        # T counts
        self.T_L = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
        
        self.H = [[1,0,1,1,1,1,1,0,1,1,0,1],[1,0,1,1,0,1,1,1,1,1,0,1],[1,0,1,1,1,1,1,1,1,1,0,1]]
        self.L = [1,0,0,1,0,0,1,0,0,1,1,1]
    # HELPER FUNCTIONS
    # Creates a list of size "listLength" where the values are disctly random in the range [1,24]
    # 
    def randomTuple(self, listLength, tuple_size):
        distinctVals = dict()
        A = [None] * listLength
        for i in range(0,listLength):
            distinct = False
            while not distinct:
                new_val = randrange(0,listLength)
                if(distinctVals.get(new_val) == None):
                    A[i] = new_val
                    distinctVals[new_val] = 1
                    distinct = True
        return list.copy([A[j:j + tuple_size] for j in range(0,listLength, tuple_size)])
    # Creates Sm set list that has uses the values from the j_set as the indexes to access the letter_list values
    def buildSmSet(self, letter_list, j_set, tuple_size):
        Sm_set = [None]*len(letter_list)
        Sm_set = [Sm_set[j:j + tuple_size] for j in range(0,len(Sm_set), tuple_size)]
        for i in range(0,len(Sm_set)):
            for j in range (0,len(Sm_set[i])):
                Sm_set[i][j] = letter_list[j_set[i][j]]
        return Sm_set
    # Trains the H or L Class based on the Smset
    # train_HSet: True, trains H class..... False, trains L class
    def trainSm(self, Sm_set, train_HSet):
        str_val = ""
        if train_HSet:
            for i in range(0,len(Sm_set)):
                for j in range(0,len(Sm_set[i])):
                    str_val = ''.join([str(Item) for Item in Sm_set[i]])
                    self.T_H[i][int(str_val,2)] +=1
        else: 
            for i in range(0,len(Sm_set)):
                for j in range(0,len(Sm_set[i])):
                    str_val = ''.join([str(Item) for Item in Sm_set[i]])
                    self.T_L[i][int(str_val,2)] +=1
    # Takes any tuple and returns the integer value of it
    def tuple_to_decimal(self,A):
        sum = 0
        power = 0
        for i in reversed(A):
            if(i != 0):
                sum+=2**power
            power+=1
        return sum
    # Grabs the string representations of the lines in the file "file_name", this function returns a list of lists
    def grabData(self, file_name):
        read_file = open(file_name,"r")
        line_read = read_file.readlines()
        new_list = [[]]
        for line in line_read:
            new_list.append(list.copy(ast.literal_eval(line)))
        del new_list[:1]
        return new_list
    # Prints the trained data set based on the letter
    def print_training_set(self,letter):
        letter = letter.lower();
        if letter == "h":
            print("TRAINED SET FOR: H")
            for i in range(0,len(self.T_H)):
                print(self.T_H[i])
        elif letter == "l":
            print("TRAINED SET FOR: L")
            for i in range(0,len(self.T_L)):
                print(self.T_L[i])
    # Neural Network Tools
    # Generates "dataSize" random H arrays with a randomized noise index. ALl the random array get stored in "file_name"
    def generateHData(self,file_name, dataSize):
        current_file = open(file_name,"w")
        for i in range(0, dataSize):
            rand_H_copy = randrange(0,3) # Picking a random H template to use
            new_H = list.copy(self.H[rand_H_copy]) # Making a copy of the H template
            pixel_noise = randrange(0,12) # Picking the random noise pixel
            new_H[pixel_noise] = 1-new_H[pixel_noise] # Negating the pixel value at the noise index
            print(new_H,file=current_file)
        current_file.close()
    # Generates "dataSize" random L arrays with a randomized noise index. ALl the random array get stored in "file_name"
    def generateLData(self,file_name, dataSize):
        current_file = open(file_name,"w")
        for i in range(0, dataSize):
            new_H = list.copy(self.L) # Making a copy of the L template
            pixel_noise = randrange(0,12) # Picking the random noise pixel
            new_H[pixel_noise] = 1-new_H[pixel_noise] # Negating the pixel value at the noise index
            print(new_H,file=current_file)
        current_file.close()
    # CWO
    def sampleTesting(self,sample_data_fname):
        pass
    # CWO: Takes in an H dataset from a text file and updates the T_H arrays based on the tuple sizes
    def trainHSet(self, data_fname, tuple_size):
        letter_data = self.grabData(data_fname)
        j_set = self.randomTuple(len(letter_data[0]),tuple_size)
        for i in letter_data:
            Sm_set = self.buildSmSet(i,j_set,tuple_size)
            self.trainSm(Sm_set,True)
        # PRINTING THE self.T_H trained set
        self.print_training_set("H")
    # CWO: Takes in an H dataset from a text file and updates the T_H arrays based on the tuple sizes
    def trainLSet(self, data_fname):
        letter_data = self.grabData(data_fname)
        #Increments corresponding value of sample sets in the; ie if j1 = [0,1,0] then Lj1[2] += 1 
        for arr in letter_data:
            temp_j1 = str(arr[3-1]) + str(arr[7-1]) + str(arr[9-1])
            temp_j2 = str(arr[1-1]) + str(arr[4-1]) + str(arr[12-1])
            temp_j3 = str(arr[5-1]) + str(arr[6-1]) + str(arr[11-1])
            temp_j4 = str(arr[2-1]) + str(arr[8-1]) + str(arr[10-1])
            self.T_L[0][int(temp_j1,2)]  = self.T_L[0][int(temp_j1,2)] + 1
            self.T_L[1][int(temp_j2,2)] = self.T_L[1][int(temp_j2,2)] + 1
            self.T_L[2][int(temp_j3,2)] = self.T_L[2][int(temp_j3,2)] + 1
            self.T_L[3][int(temp_j4,2)] =  self.T_L[3][int(temp_j4,2)] + 1
        self.print_training_set("L")