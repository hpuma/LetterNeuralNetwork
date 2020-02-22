from random import randrange
import ast
class LetterNNET:
    def __init__(self):
        # Class Training Lists:
        # Letter Indexing: Top -> Bottom 0,1,2,3,...n-1 
        # H Counts containing the tuple occurance after training
        self.T_H = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
        # T counts containing the tuple occurance after training
        self.T_L = [[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0]]
        # Class Jm sets that are used for training and sampling
        # Letter_Jm: A set containing the indices of the sampled pixels when training and sampling
        self.H_Jm = None
        self.L_Jm = None
        # Templates for each letter class, this is used to generate a list with a random noise
        self.H = [[1,0,1,1,1,1,1,0,1,1,0,1],[1,0,1,1,0,1,1,1,1,1,0,1],[1,0,1,1,1,1,1,1,1,1,0,1]]
        self.L = [1,0,0,1,0,0,1,0,0,1,1,1]
    # DATA GENERATOR HELPER FUNCTIONS
    # Generates a H or L class list with "num_noise" randomized pixels as noise
    # Noise: A pixel (list value) that gets its value negated
    def generateHList(self, num_noise:int)->list:
        new_h = list.copy(self.H[randrange(0, 3)]) # Picking a random H template
        h_length = len(new_h)
        add_noise = 0
        while add_noise != num_noise:
            pixel_noise = randrange(0, h_length) # Picking the random noise pixel
            new_h[pixel_noise] = 1 - new_h[pixel_noise] # Negating the pixel value at the noise index
            add_noise += 1 # Incrementing the number of noise pixels
        return new_h
    # Same implementation as generateHList but instead for L list
    def generateLList(self, num_noise:int)->list:
        new_l = list.copy(self.L) # Picking a random copy of the L template
        l_length = len(new_l)
        add_noise = 0
        while add_noise != num_noise:
            pixel_noise = randrange(0, l_length) # Picking the random noise pixel
            new_l[pixel_noise] = 1 - new_l[pixel_noise] # Negating the pixel value at the noise index
            add_noise += 1
        return new_l
    # Generates "data_size" random H lists with "num_noise" random pixels as noise for each list
    # ALl the random lists get stored in "file_name"
    def generateHData(self, file_name:str, data_size:int, num_noise:int)->None:
        current_file = open(file_name,"w")
        for i in range(0, data_size):
            new_h = self.generateHList(num_noise)
            print(new_h,file=current_file)
        current_file.close()
    # Generates "data_size" random L lists with "num_noise" random pixels as noise for each list.
    # ALl the random lists get stored in "file_name"
    def generateLData(self, file_name:str, data_size:int, num_noise:int)->None:
        current_file = open(file_name,"w")
        for i in range(0, data_size):
            new_l = self.generateLList(num_noise)
            print(new_l,file=current_file)
        current_file.close()
   # Generates a sample of randomized H or L class lists with the same amount of noise
   # NOTE: The very last list will always be the sampleData list, which is crucial for the program to know the original class for each list
   # The list "sampleData" is a 2D list containing the class idendifier for each sublist in sample file
   # For each list i in the Sample:
   # Value: 0 at list i - Belongs to L Class or
   # Value: 1 at list i - Belongs to H class 
    def generateSample(self, file_name:str, sample_size:int, num_noise:int)->None:
        current_file = open(file_name, "w")
        sampleData = [] # IMPORTANT: keeps track of the correct letter at index i of sample_data
        for i in range(0, sample_size):
            if randrange(1, 11)%2 == 0:
                new_list = self.generateHList(num_noise)
                sampleData.append(1)
            else:
                new_list = self.generateLList(num_noise)
                sampleData.append(0)
            print(new_list, file=current_file)
        print(sampleData, file=current_file, end="")
    # Retrieves and removes the sample_list list from the sample_data list
    # The sample_list list should NOT be included in sample_data list !
    def getSampleList(self, sample_data:list)->list:
        sampleList = sample_data[-1]
        sample_data.pop()
        return sampleList
    # Gets the letter class counts from the "sample_data"" list
    # Index : 0 -  Class L
    # Index : 1 - Class H
    def getSampleLetters(self, sample_data:list)->list:
        letterData = [0,0]
        for i in sample_data:
                letterData[i]+=1
        return letterData
    # HELPER FUNCTIONS
    # Takes in a list and then evenly divides it into "tuple_size" tuples within the list
    def divideList(self, A:list, tuple_size:int)->list:
        alen = len(A)
        return list.copy([A[j:j + tuple_size] for j in range(0, alen, tuple_size)])
    # Recieves a list with binary representation returns its integer value
    # We first turn the entire list into a string, then we use python int() to convert from base 2 to base 10.
    # e.g [1,0,1] -> "101" -> int("101", 2) return 5
    def tuple_to_int(self, A:list)->int:
        return int("".join([str(i) for i in A]), 2)

    # Computes the integer value of the entire input_list based on the H or L trained class counts T_H or T_L
    # Note: must specify using the H or L Sm set attributes
    def compute_list_val(self, input_list:list, sample_from:str, tuple_size:int)->int:
        sample_from = sample_from.lower()
        list_sum = 0
        j = 0 # Used to access the self.T_Letter list      
        if 'h' in sample_from:
            list_Sm = self.build_SmSet(input_list, self.H_Jm, tuple_size)
            for i in list_Sm:
                list_sum += self.T_H[j][self.tuple_to_int(i)] # Gets the sum of the n tuples
                j += 1
            return list_sum
        elif 'l' in sample_from:
            list_Sm = self.build_SmSet(input_list,self.L_Jm, tuple_size)
            for i in list_Sm:
                list_sum += self.T_L[j][self.tuple_to_int(i)] # Gets the sum of the n tuples
                j += 1
            return list_sum
    # Prints the trained data set based on the letter class chosen
    def print_training_set(self, letter:str)->None:
        letter = letter.lower();
        if 'h' in letter:
            print("TRAINED SET FOR: H")
            for i in self.T_H:
                print(i)
        elif 'l' in letter:
            print("TRAINED SET FOR: L")
            for i in self.T_L:
                print(i)
    # NEURAL NETWORK FUNCTIONS ------------------------------------------------------------------------------------------------------------

    # Grabs the list representations of the lines in the file "file_name"
    # This function returns a 2D list of all the lists from the file
    def grabData(self, file_name:str)->list:          
        read_file = open(file_name, "r")
        line_read = read_file.readlines()
        return [list.copy(ast.literal_eval(line)) for line in line_read]

    # Creates a list of size "list_length" where the values are distinctly random in the range [0,listLength)
    # The list is divided evenly by "tuple_size" sized tuples
    # The Jm set is a list of randomly chosen index values for sampling
    def build_JmSet(self, list_length:int, tuple_size:int)->list:
        distinctVals = dict()
        A = [None] * list_length
        for i in range(0, list_length):
            distinct = False
            while not distinct:
                new_val = randrange(0, list_length)
                if(distinctVals.get(new_val) == None):
                    A[i] = new_val
                    distinctVals[new_val] = 1
                    distinct = True
        return self.divideList(A, tuple_size)
    # Creates the Sm set list that uses the values from the Jm_set as the indexes to access the letter_list values
    # We are using the randomized values as index value from the jm_set within the letter_list
    def build_SmSet(self, letter_list:list, Jm_set:list, tuple_size:int)->list:
        Sm_set = [None] * len(letter_list)
        Sm_set = self.divideList(Sm_set, tuple_size)
        for i in range(0, len(Sm_set)):
            for j in range (0, len(Sm_set[i])):
                Sm_set[i][j] = letter_list[Jm_set[i][j]]
        return Sm_set
    # Trains the H or L Class based on the Sm_set
    # train_HSet: Boolean
    # True, trains H class
    # False, trains L class
    def train_Sm(self, Sm_set:list, train_HSet:bool)->None:
        tuuple_val = 0
        if train_HSet:
            for i in range(0, len(Sm_set)):
                tuple_val = self.tuple_to_int(Sm_set[i])
                self.T_H[i][tuple_val] += 1
        else: 
            for i in range(0, len(Sm_set)):
                tuple_val = self.tuple_to_int(Sm_set[i])
                self.T_L[i][tuple_val] += 1
    # Takes in an H dataset from a text file and updates the T_H list based on the integer values of the n sized tuples
    # input_Jm: is an optional Jm set that can be used, if none is provided then the self.H_Jm list will be used
    def trainHSet(self, data_fname:str, tuple_size:int, input_Jm=None)->None:
        letter_data = self.grabData(data_fname)
        if input_Jm == None:
            input_Jm = self.build_JmSet(len(letter_data[0]), tuple_size)
        if len(input_Jm) != int((len(letter_data[0])/tuple_size)):
           input_Jm = self.divideList(input_Jm, tuple_size) 
        self.H_Jm = input_Jm
        for i in letter_data:
            Sm_set = self.build_SmSet(i, self.H_Jm, tuple_size)
            self.train_Sm(Sm_set, True)
        # PRINTING THE self.T_H trained set
        self.print_training_set("H")
    # Takes in an L dataset from the "data_fname" file and updates the T_L list based on each tuple value
    # input_Jm: is an optional Jm set that can be used, if none is provided then the self.L_Jm list will be used
    def trainLSet(self, data_fname:str, tuple_size:int, input_Jm=None)->None:
        letter_data = self.grabData(data_fname)
        if input_Jm == None:
            input_Jm = self.build_JmSet(len(letter_data[0]), tuple_size)
        if len(input_Jm) != (len(letter_data[0])/tuple_size):
           input_Jm = self.divideList(input_Jm, tuple_size)
        self.L_Jm = input_Jm
        for i in letter_data:
            Sm_set = self.build_SmSet(i, self.L_Jm, tuple_size)
            self.train_Sm(Sm_set,False)
        # PRINTING THE self.T_H trained set
        self.print_training_set("L")       
    # Uses the trained H and L lists to determine whether the letter lists in the "sample_data_fname" file
    # NOTE: The sample file must be generated by the "generateSample" function! or you can make it yourself but 
    # make sure that the very last list is the "sample_data" list where 1 is H and 0 is L for each line in the "sample_data_fname" file!!
    def sampleTesting(self, sample_data_fname:str, tuple_size:int)->list:
        sample_data = self.grabData(sample_data_fname) # Gets all the lines from the sample file
        sample_list = self.getSampleList(sample_data) # Gets the important sampleData list from the sample file, the correct letter values
        sample_letters = self.getSampleLetters(sample_list) # Gets the class counts of each letter from the sample file by using the sampleData list
        # Number of letter counts determined by the program
        H_count = 0 
        L_count = 0 
        guess_list = []
        # Temp variables: Sum variables that correspond the the list in the sample file, This is the total sum from the Trained Ls for each list
        # These sums are used by the computer to determine whether the sample lists is a CLASS H  OR CLASS L
        # The program uses the greatest sum to determine the letter class
        H_sum = 0 
        L_sum = 0

        current_letter = 0 # The index for the sample_data list so that we know the actual class of the sample list
        correct = 0 # Keeps track of the correct guesses made by the program

        for i in sample_data: # For each list in the sample list from the sample file
            correct_letter = sample_list[current_letter] # The correct letter class of the current list 
            H_sum = self.compute_list_val(i, "H",tuple_size) # Value determines how likley the current letter is H
            L_sum = self.compute_list_val(i, "L",tuple_size) # Value determines how likley the current letter is L
            # First, we print out sample list and the correct letter class for the current value
            print("Letter:",current_letter+1,end="\t\t")
            print(i,"A:",sep="\t",end="\t")
            if correct_letter == 1:
                print("H",end="\t")
            elif correct_letter == 0:
                print("L",end="\t")
            # Then, we print the program's guess based on the H_sum and L_sum
            # We also update the number of correct guesses accordingly
            print("G:",end="\t")
            if H_sum > L_sum: # The programdetermines the current list to be class H
                guess_list.append(1)
                H_count += 1 # Update number of H guesses
                if correct_letter == 1: # When we guess H and the correct letter is H
                    correct += 1
                    print("H")
                else: # The guess was H but the letter was actually L
                    print("H\tINCORRECT")
            else:  # The program determines the current list to be class L
                guess_list.append(0)
                L_count += 1
                if correct_letter == 0: # When the guess is L and the actual letter is L
                    correct += 1
                    print("L")
                else: # The guess was L but the actual letter was H 
                    print("L\tINCORRECT")
            current_letter += 1
        # RESULTS ------------------------------------------------------------
        # Prints the number of H and L guessed and the accuracy of the program
        print("\nActual Count:",end="\t")
        print("H:",sample_letters[1],"L:",sample_letters[0],sep="\t")
        print("Guess Count:",end="\t")
        print("H:",H_count,"L:",L_count,sep="\t")
        print("Correct:",correct,"\nIncorrect:",len(sample_data)-correct)
        print("Accuracy:\t",(correct/len(sample_data))*100,"%")
        return guess_list