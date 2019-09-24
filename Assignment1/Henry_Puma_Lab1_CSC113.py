# Henry Puma 
# CSC 11300 - Morning Session
# NOTE: Functions were not required, it was a bit overkill.
import math # Importing math module to use math.pi
# min: minutes
# sec: seconds
# Output: The total amount of seconds given a number of minutes and seconds.
def timeCalc(min,sec):
    return ((min*60) + sec)
# a: The length of side a
# Output: The number of cubes that could fit inside a rectangular prism with sides a, 2a , 3a.
def shapeCalc(a):
    rect = a * (2*a) *(3*a) # Calculates the volume of the rectange l * w * h == a * 2*a * 3*a.
    cube = math.pow(a,3) # Calculates the volume of a cube a^3.
    return (rect/cube) # Returns the Rectangle divided by the cube, which is the amount of times the cube could fit into the rectangle.
# r: circle's radius
# Output: The volume of a sphere.
def circle(r):
    return  ((4/3)*math.pi*math.pow(r,2)) # Sphere's formula.
#F: Fahrenheit
#C: Celsius 
# Output: The temperature conversion depending on whats given.
def tempChange(F=0,C=0):
    if(F and C ==0): # Checks if only a Fahrenheit value is given and not a Celcius.
        return ((F-32) * (5/9)) # Formula for F --> C 
    elif(F == 0 and C): # Checks if only a Celsius value is given and not a Fahrenheit.
        return (C*(9/5)+32) # Formula for F --> C 
    else: return 0
# a: The length of side a
# Output: The number of cubes that could fit inside a rectangle.
def shapeCalc(a):
    rect = a * (2*a) *(3*a) # Calculates the volume of the rectange l * w * h.
    cube = math.pow(a,3) # Calculates the volume of a cube a^3.
    return (rect/cube) # Returns the Rectangle divided by the cube, which is the amount of times the cube could fit into the rectangle.
# Submitted Answers
print('There are ',(42*60)+42," seconds in 42 minutes and 42 seconds") 
# A - Because for every minute there are 60 seconds, we do 42 min * 60 seconds to convert from minutes to seconds, 
# then we just add on the given 42 seconds to find the total which is 2562 seconds.

print('The volume of a sphere with radius 4:\t',(4/3)*math.pi*(4**3)) # Volume of sphere with radius 4: 268.08 
print('The volume of a sphere with radius 6:\t',(4/3)*math.pi*(6**3)) # Volume of sphere with raidus 5: 904.77
# B - We know the volume of a sphere is (4/3)*pi*r^3 , all we have to do is plug in 4 and 6 for the formula.

print('-40 Fahrenheit to Celcius:\t',(-40-32)*(5/9)) 
print('-40 Celsius to Fahrenheit:\t',(-40*(9/5)+32)) 
# C - Using the F -> C and C -> F formulas to find that -40 is the same in both F and C.

a = 2 # Side a. 
rect = a * (2*a) *(3*a) # Calculates the volume of the rectangular prism l * w * h == a * 2*a * 3*a.
C = a**3 # Calculates the volume of cube C a^3.
print('The number of cubes that could fit inside a rectangular prism is:\t', (rect/C)) # 6 cubes could fit into the rectangular prism.
# D - Prints the Rectangle divided by the cube, which is the amount of times the cube could fit into the rectangle.