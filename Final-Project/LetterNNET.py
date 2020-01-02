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
        # Templates for each letter class, this is used to generate an array with a random noise
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
    # To accomplish this we turn the list into a string and use the python int() to turn it into a string, we pass 2 to let it know that we are going from base 2 to base 10
    def tuple_to_int(self,A):
        return int("".join([str(i) for i in A]),2)
    def divideList(self, A, tuple_size):
        return list.copy([A[j:j + tuple_size] for j in range(0,len(A), tuple_size)])
    # Note: must specify using the H or L Sm set attributes
    # Computes the value of the input_list based on the H or L class
    def compute_list_val(self, input_list, sample_from, tuple_size): #
        sample_from = sample_from.lower()
        list_sum = 0
        j = 0        
        if 'h' in sample_from:
            list_Sm = self.build_SmSet(input_list, self.H_Jm, tuple_size)
            for i in list_Sm:
                list_sum += self.T_H[j][self.tuple_to_int(i)] # Gets the sum of the n tuples
                j+=1
            return list_sum
        elif 'l' in sample_from:
            list_Sm = self.build_SmSet(input_list,self.L_Jm, tuple_size)
            for i in list_Sm:
                list_sum += self.T_L[j][self.tuple_to_int(i)] # Gets the sum of the n tuples
                j+=1
            return list_sum
    # Prints the trained data set based on the letter
    def print_training_set(self,letter):
        letter = letter.lower();
        if 'h' in letter:
            print("TRAINED SET FOR: H")
            for i in self.T_H:
                print(i)
        elif 'l' in letter:
            print("TRAINED SET FOR: L")
            for i in self.T_L:
                print(i)
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
        return self.divideList(A,tuple_size)
    # Creates Sm set list that has uses the values from the jm_set as the indexes to access the letter_list values
    def build_SmSet(self, letter_list, jm_set, tuple_size):
        Sm_set = [None]*len(letter_list)
        Sm_set = self.divideList(Sm_set,tuple_size)
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
                str_val = self.tuple_to_int(Sm_set[i])
                self.T_H[i][str_val] +=1
        else: 
            for i in range(0,len(Sm_set)):
                str_val = self.tuple_to_int(Sm_set[i])
                self.T_L[i][str_val] += 1
    # Neural Network Tools
    # Generates a H or L class list with a randomized pixel as noise
    def generateHList(self, num_noise):
        new_h = list.copy(self.H[randrange(0,3)]) # Making a copy of the H template
        add_noise = 0
        while add_noise != num_noise:
            pixel_noise = randrange(0,12) # Picking the random noise pixel
            new_h[pixel_noise] = 1-new_h[pixel_noise] # Negating the pixel value at the noise index
            add_noise += 1
        return new_h
    def generateLList(self, num_noise):
        new_l = list.copy(self.L) # Making a copy of the L template
        add_noise = 0
        while add_noise != num_noise:
            pixel_noise = randrange(0,12) # Picking the random noise pixel
            new_l[pixel_noise] = 1-new_l[pixel_noise] # Negating the pixel value at the noise index
            add_noise+=1
        return new_l
    # TODO : MAKE SAMPLE GENERATOR THAT MAKES A SAMPLE TO TEST ALONG WITH RETURNING AN ARRAY WHETHER THE THE SAMPLE LINE IS AN H OR L
    def generateSample(self, file_name, sampleSize, dataNoise):
        current_file = open(file_name,"w")
        sampleData = []
        for i in range(0,sampleSize):
            if randrange(1,10)%2 == 0:
                new_list = self.generateHList(dataNoise)
                sampleData.append(1)
            else:
                new_list = self.generateLList(dataNoise)
                sampleData.append(0)
            print(new_list,file=current_file)
        print(sampleData,file=current_file,end="")
    # Gets the last list from the sample data because it is the only list that tells us which letters were randomly generated
    def getSampleList(self, sampleData):
        sampleList = sampleData[-1]
        sampleData.pop()
        return sampleList
    def getSampleLetters(self, sampleList):
        letterData = [0,0]
        for i in sampleList:
            if i == 0:
                letterData[i]+=1
            elif i == 1:
                letterData[i]+=1
        return letterData

    # Generates "dataSize" random H arrays with a randomized noise index. ALl the random array get stored in "file_name"
    def generateHData(self, file_name, dataSize, dataNoise):
        current_file = open(file_name,"w")
        for i in range(0, dataSize):
            new_h = self.generateHList(dataNoise)
            print(new_h,file=current_file)
        current_file.close()
    # Generates "dataSize" random L arrays with a randomized noise index. ALl the random array get stored in "file_name"
    def generateLData(self, file_name, dataSize, dataNoise):
        current_file = open(file_name,"w")
        for i in range(0, dataSize):
            new_l = self.generateLList(dataNoise)
            print(new_l,file=current_file)
        current_file.close()
    # Takes in an H dataset from a text file and updates the T_H arrays based on the tuple sizes
    def trainHSet(self, data_fname, tuple_size):
        letter_data = self.grabData(data_fname)
        letter_length = len(letter_data[0])
        self.H_Jm = self.build_JmSet(letter_length,tuple_size)
        for i in letter_data:
            Sm_set = self.build_SmSet(i,self.H_Jm,tuple_size)
            self.train_Sm(Sm_set,True)
            
        # PRINTING THE self.T_H trained set
        self.print_training_set("H")
    # Takes in an H dataset from a text file and updates the T_H arrays based on the tuple sizes
    def trainLSet(self, data_fname, tuple_size):
        letter_data = self.grabData(data_fname)
        letter_length = len(letter_data[0])
        self.L_Jm = self.build_JmSet(letter_length,tuple_size)
        for i in letter_data:
            Sm_set = self.build_SmSet(i,self.L_Jm,tuple_size)
            self.train_Sm(Sm_set,False)
        # PRINTING THE self.T_H trained set
        self.print_training_set("L")       
    # CWO: 
    def sampleTesting(self, sample_data_fname,tuple_size):
        sample_data = self.grabData(sample_data_fname)
        sample_list = self.getSampleList(sample_data)
        sample_letters = self.getSampleLetters(sample_list)
        H_count = 0
        L_count = 0
        H_sum = 0
        L_sum = 0
        current_letter = 0
        correct = 0
        for i in sample_data:
            correct_letter = sample_list[current_letter] 
            H_sum = self.compute_list_val(i,"H",tuple_size)
            L_sum = self.compute_list_val(i,"L",tuple_size)
            print("Letter List:",current_letter,"\t",i,end="\t")
            print("Actual:\t",end="")
            if correct_letter == 1:
                print("H",end="\t\t")
            elif correct_letter == 0:
                print("L",end="\t\t")
            print("Guess:",end="\t")
            if H_sum > L_sum:
                H_count+=1
                print("H")
                if correct_letter == 1:
                    correct+=1
            else:
                L_count+=1
                print("L")
                if correct_letter == 0:
                    correct+=1
            current_letter+=1
        # Prints the number of H and L guessed
        print("Actual Count:",end="\t")
        print("H:\t",sample_letters[1],end="\t")
        print("L:\t",sample_letters[0])
        print("Guess Count:",end="\t")
        print("H:\t",H_count,end="\t")
        print("L:\t",L_count)
        print("Accuracy:\t",correct/len(sample_data))