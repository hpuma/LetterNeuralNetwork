from LetterNNET import LetterNNET

#lists of known L images for testing
l1 = [1,0,0,1,0,0,1,0,0,1,1,1]
l2 = [1,0,0,1,0,0,1,1,0,0,0,0]
l3 = [1,0,0,1,0,0,1,0,0,1,1,0]


#For each of the following, indicies corrrespond to exact binary conversion ['000','001','010','011','100','101','110','111']
#This is a profile of the letter L
Lj1 = [0,0,0,0,0,0,0,0]  #sample set j1 testing indicies: (3,7,9)
Lj2 = [0,0,0,0,0,0,0,0]  #sample set j2 testing indicies: (1,4,12)
Lj3 = [0,0,0,0,0,0,0,0]  #sample set j3 testing indicies: (5,6,11)
Lj4 = [0,0,0,0,0,0,0,0]  #sample set j4 testing indicies: (2,8,10)


def class_L_training(arr):  
    """ Takes in array that is known to represent the letter L and builds the profile for a letter L"""

    #Builds j1,j2,j3,j4 as strings; ie (1,0,1) -> '101'
    temp_j1 = str(arr[3-1]) + str(arr[7-1]) + str(arr[9-1])
    temp_j2 = str(arr[1-1]) + str(arr[4-1]) + str(arr[12-1])
    temp_j3 = str(arr[5-1]) + str(arr[6-1]) + str(arr[11-1])
    temp_j4 = str(arr[2-1]) + str(arr[8-1]) + str(arr[10-1])
    
    #Increments corresponding value of sample sets in the; ie if j1 = [0,1,0] then Lj1[2] += 1 
    Lj1[int(temp_j1,2)] += 1
    Lj2[int(temp_j2,2)] += 1
    Lj3[int(temp_j3,2)] += 1
    Lj4[int(temp_j4,2)] += 1

test1 = LetterNNET()
testarr = test1.grabData('L_Training_set.txt')
print(testarr)


i = 1
while i <=199:
    class_L_training(testarr[i])
    i+=1

print(Lj1)
print(Lj2)
print(Lj3)
print(Lj4)