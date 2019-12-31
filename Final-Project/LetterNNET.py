from random import randrange
import ast
class LetterNNET:
    def __init__(self):
        # Top -> Bottom 0,1,2,3, These arrays are the Training sets
        # H counts 
        self.T_H = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
        # T counts
        self.T_L = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
        # Storing the Jm sets used when training the letter class
        self.H_Jm = []
        self.L_Jm = []
        # Templates from each letter class, this is used to generate an array with a random noise
        self.H = [[1,0,1,1,1,1,1,0,1,1,0,1],[1,0,1,1,0,1,1,1,1,1,0,1],[1,0,1,1,1,1,1,1,1,1,0,1]]
        self.L = [1,0,0,1,0,0,1,0,0,1,1,1]
    # HELPER FUNCTIONS
    # Grabs the string representations of the lines in the file "file_name", this function returns a list of lists
    def grabData(self, file_name):
        read_file = open(file_name,"r")
        line_read = read_file.readlines()
        data_list = []
        for line in line_read:
            data_list.append(list.copy(ast.literal_eval(line)))
        return data_list
    # Takes any tuple and returns the integer value of it
    def tuple_to_int(self,A):
        sum = 0
        power = 0
        for i in reversed(A):
            if(i != 0):
                sum+=2**power
            power+=1
        return sum
    # TODO
    def divideList(self,A, tuple_size):
        return list.copy([A[j:j + tuple_size] for j in range(0,len(A), tuple_size)])
    # Note: must specify using the H or L Sm set attributes
    def compute_list_val(self,input_list,sample_from,tuple_size): #
        sample_from = sample_from.lower()
        list_sum = 0
        if 'h' in sample_from:
            list_Sm = self.build_SmSet(input_list,self.H_Jm, tuple_size)
            j = 0
            for i in list_Sm:
                list_sum += self.T_H[j][self.tuple_to_int(i)] # Gets the sum of the n tuples
                j+=1
            return list_sum
        elif 'l' in sample_from:
            list_Sm = self.build_SmSet(input_list,self.L_Jm, tuple_size)
            j = 0
            for i in list_Sm:
                list_sum += self.T_L[j][self.tuple_to_int(i)] # Gets the sum of the n tuples
                j+=1
            return list_sum
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
    # Creates a list of size "listLength" where the values are disctly random in the range [1,24]
    def build_JmSet(self, listLength, tuple_size):
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
    # Creates Sm set list that has uses the values from the jm_set as the indexes to access the letter_list values
    def build_SmSet(self, letter_list, jm_set, tuple_size):
        Sm_set = [None]*len(letter_list)
        Sm_set = [Sm_set[j:j + tuple_size] for j in range(0,len(Sm_set), tuple_size)]
        for i in range(0,len(Sm_set)):
            for j in range (0,len(Sm_set[i])):
                Sm_set[i][j] = letter_list[jm_set[i][j]]
        return Sm_set
    # Trains the H or L Class based on the Smset
    # train_HSet: True, trains H class..... False, trains L class
    def train_Sm(self, Sm_set, train_HSet):
        str_val = 0
        if train_HSet:
            for i in range(0,len(Sm_set)):
                for j in range(0,len(Sm_set[i])):
                    str_val = self.tuple_to_int(Sm_set[i])
                    self.T_H[i][str_val] +=1
        else: 
            for i in range(0,len(Sm_set)):
                for j in range(0,len(Sm_set[i])):
                    str_val = self.tuple_to_int(Sm_set[i])
                    self.T_L[i][str_val] +=1
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
    # Takes in an H dataset from a text file and updates the T_H arrays based on the tuple sizes
    def trainHSet(self, data_fname, tuple_size):
        letter_data = self.grabData(data_fname)
        self.H_Jm = self.build_JmSet(len(letter_data[0]),tuple_size)
        for i in letter_data:
            Sm_set = self.build_SmSet(i,self.H_Jm,tuple_size)
            self.train_Sm(Sm_set,True)
        # PRINTING THE self.T_H trained set
        self.print_training_set("H")
    # Takes in an H dataset from a text file and updates the T_H arrays based on the tuple sizes
    def trainLSet(self, data_fname, tuple_size):
        letter_data = self.grabData(data_fname)
        self.L_Jm = self.build_JmSet(len(letter_data[0]),tuple_size)
        for i in letter_data:
            Sm_set = self.build_SmSet(i,self.L_Jm,tuple_size)
            self.train_Sm(Sm_set,False)
        # PRINTING THE self.T_H trained set
        self.print_training_set("L")       
    # CWO: 
    def sampleTesting(self, sample_data_fname,tuple_size):
        sample_data = self.grabData(sample_data_fname)
        H_count = 0
        L_count = 0
        H_sum = 0
        L_sum = 0
        for i in sample_data:
            H_sum = self.compute_list_val(i,"H",tuple_size)
            L_sum = self.compute_list_val(i,"L",tuple_size)
            if H_sum > L_sum:
                H_count+=1
            else:
                L_count+=1
        # Prints the number of H and L guessed
        print("H:\t",H_count)
        print("L:\t",L_count)