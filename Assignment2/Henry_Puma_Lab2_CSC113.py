import math as m
# Henry Puma 
# Professor Yuksel 
# CSC 113000 Morning session

# A Convert minutes to millisecoonds
# Example, 3 minutes should be 180,0000 milliseconds!
def minutesSeconds(minutes):
    return 60000*minutes # There are 60,000 milliseconds in each minute.
print("The number of milliseconds in 3 minutes is:\t",minutesSeconds(3))

# B Define a function to find the average of two scores
# Example: The average of scores 85,80 is 82.5 because 85+80 = 165. Avereage is 165/2 = 82.5
def testAverage(score1, score2):
    return ((score1+score2)/2)

print("The average of two test that are 85 and 80:\t",testAverage(85,80))

# C Use mathmoduleimport to use square rootand compute the roots of a quatratic equation.
# Example a = 1 , b = 3, c = 2
def quadRoots(a,b,c):
    discriminant  = b**2 - (4*a*c)
    x1 =(-b + m.sqrt(discriminant))/(2*a)
    x2 =(-b - m.sqrt(discriminant))/(2*a)
    return x1,x2
# D Define a function to convert Kelvin to Réaumur, 
# then Réaumur to Celsius. Use different functions, and call one inside the other,if necessary.

# Supplementary function that converts from kelvin to Raumer
def KelvinRaumer(kelvin):
    return((kelvin-273.15)*0.8)

# Takes Kelvin -> Raumer -> Celsius
def KelvinRaumerCelsius(kelvin):
    raumerVal = KelvinRaumer(kelvin)
    return(raumerVal*(4/5))

print("273.15 C to Rauner is:\t",KelvinRaumerCelsius(273.15))

# E Say you have a cube with side of n. And you have some amount of marbles (round,
# sphere) with radius n/4 How many marbles can you fit in the cube? Obtain the solution
# with the use of functions. 
def marblesFit(n):
    r = n/4 # Find the radius of the marbles by dividing it by 4.
    cubeVolume = n**3 # Take the volume of a cube.
    marblesVolume  = (4/3)*m.pi*r**3 # Takes the volume of the marble.
    return cubeVolume/marblesVolume # Divides the number of marbles that could fit into the cube.
# How many marbles can fit into a cube where n = 5?
print("Marbles with radius n/4 fits ",marblesFit(5)," times in a cube with length n")

# F 
# Supplementary functions to print out each line, depending on whether its column or row.
def printRow():
    print('''^ - ^ - ^^ - ^ - ^^ - ^ - ^^ - ^ - ^^''')
def printColumn():
    print('''i        i        i        i        i''')

# Supplementary function to print a 1 x 4 boxes.
# NOTE: This does not print the first row.
def printOneFour():
    printColumn()
    printColumn()
    printColumn()
    printColumn()
    printRow()

# Calls the the rowPrinter, then proceeds to print the 1x4.
def printGrid():
    printRow()
    printOneFour()
    printOneFour()
    printOneFour()
    printOneFour()
    
# This actually prints the grid.
printGrid()