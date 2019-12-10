# Strings 11/26/19
# Strings are immutable in Python

# Accessing a string 
# test = "Hello World"
# [start:stop:countBy]
# print(test[0:-1:1])
# print(test[::2])

# Copying a string 
# my_str = "hi mom"
# new_str = my_str[:] # Used to create a distinct copy of a sequence 
# print(my_str,new_str,sep="\n")

# How can we reverse a string?
# test = "Hello_World"
# print(test[::-1])

# String opterations
# Printing each individual element and it's associated type
# new_str = "hi mom"
# for i in new_str:
#     print(i,type(i),end="\n")

# Repeats the same string over and over again
# a = "spam"
# print (a*3)

# Checking for substrings
# my_str = "aabbccdd"
# sub = "bcc"
# print(sub in my_str)

# Turning spam to slam, splicing an array
# my_str = "spam"
# new_str = my_str[:1] + 'l'+my_str[2:]
# print(new_str)

# Finding the index of a character in a string
# my_str = "he had the bat"
# print(my_str.find('t',8))
# print(my_str[my_str.find('t')+1:].find('t'))

# Important String methods
# .join( ).strip() .split()

December 10 2019
# pass keyword used to tell the python interpreter that you are leaving the portion of a class or function blank.
# self. keyword <=> this.