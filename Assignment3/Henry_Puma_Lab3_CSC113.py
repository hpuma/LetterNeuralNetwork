# Henry Puma CSC 11300 Exercise 3
import math

# Question 1 -- DONE.
def perfectNum():
  try:
    program_continue = 1
    while(program_continue):
      user_number = int(input('Please enter the number you want to check for perfect number\n'))
      divisor_sum = 0
      for i in range(1,user_number):
        if(user_number%i== 0):
          divisor_sum+=i

      if divisor_sum == user_number and ((divisor_sum + user_number)/2)== user_number:
        print('The number', user_number, 'is a perfect number!',sep=' ')
      else:
        print('The number', user_number, 'is NOT a perfect number!',sep=' ')

      program_continue = abs(int(input('\nEnter a non-zero number to continue.\n\tTo terminate the program, please enter 0\n')))
  except ValueError:
    print('You have entered an invalid integer.')
  except TypeError:
    print('You have entered an invalid type')

# Question 2 --- DONE.
def positiveDivisor():
    user_input = 0
    user_input = int(input('Please enter a positive integer to check for its possible divisors\n'))
    print('\nThe positive integer divisors of', user_input, 'are',sep=' ',end='\n')
    current_divisor = user_input
    while current_divisor >= 1:
        if user_input%current_divisor == 0:
          print(current_divisor)
        current_divisor -=1

# Question 3 --- DONE.
# x1,y1 is a 
# x1,y2 is b 
# x3,y3 is c
# ab = A , bc = B, ca = C
def isTriangle():
  try:
    program_continue = 1
    while(program_continue):
      x1 = int(input('PLEASE ENTER\nX1:\t'))
      y1 = int(input("Y1:\t"))
      x2 = int(input('\nPLEASE ENTER\nX2:\t'))
      y2 = int(input('Y2:\t'))
      x3 = int(input('\nPLEASE ENTER\nX3:\t'))
      y3 = int(input('Y3:\t'))

      # Computing side lengths 
      length_A = math.sqrt(math.pow(x1-x2,2) + math.pow(y1-y2,2))
      length_B = math.sqrt(math.pow(x3-x2,2) + math.pow(y3-y2,2))
      length_C = math.sqrt(math.pow(x1-x3,2) + math.pow(y1-y3,2))
      if(length_A > abs(length_B - length_C)):
        print('\nThe entered points form a triangle!')
      else:
        print('\nThe entered points do not form a triangle!')
      # Checking if the user wants to continue.
      program_continue = abs(int(input('\nEnter a non-zero number to continue.\n\tTo terminate the program, please enter 0\n')))
  except ValueError:
    print('You have entered an invalid value')
  except TypeError:
    print('You have entered an invalid type')

# Question 4 --- DONE.
def findPrime():
  program_continue = 1
  while(program_continue):
    num1 = int(input('Please enter the first bound number\n'))
    num2 = int(input('\nPlease enter the second bound number\n'))
    # Checking that the bounds are valid numbers.
    if (num1 <= 0 or num2 <= 0):
      print('One of the bounds was an improper value!\n')
      return;
    print('The Prime numbers between',num1,'and',num2,'are:',sep=' ',end='\n\n')

    for i in range(min(num1,num2),max(num1,num2)+1):
      # As long as we are not checking 1, then find the prime number.
      if i != 1:
        isPrime = True
        for j in range(2, i//2 +1):
          if i%j == 0:
            isPrime = False
            break
        if(isPrime):
          print(i)
    # Checking if the user wants to continue.
    program_continue = abs(int(input('\nEnter a non-zero number to continue. To terminate the program, Enter 0\n')))

# Question 5
def possibleSeating():
  program_continue = 1
  mult_count = 1
  while(program_continue):
    user_input = int(input('Please enter the number of people seated\n'))
    for i in range (1,user_input+1):
      mult_count*=i
    print('There are',mult_count,'different seating arrangments for',user_input,'people!',sep=' ',end= '\n')
    program_continue = abs(int(input('\nEnter a non-zero number to continue.\n\tTo terminate the program, please enter 0\n')))
    
# Calling all functions.
print('\nQUESTION 1:\n')
perfectNum()
print('\nQUESTION 2:\n')
positiveDivisor()
print('\nQUESTION 3:\n')
isTriangle()
print('\nQUESTION 4:\n')
findPrime()
print('\nQUESTION 5:\n')
possibleSeating()