'''
# print comment
x = 5
y = "John"
print (x)
print (y) 
# words in programming are called strings
# 5 = Integers = Int
# "Hello" word = string
# Booleans = (0,1) Example true/false 

# variables are case sensitive
a = 4
A = "Bob"
print (a, A)
# A will not override a
# = in programming means "assigned to" Example 5 is assigned to variable x

# legal variable names 
# a variable must start with a letter
# It CANNOT start with a number
# Is case sensitive is # Age and CANNOT contain alpha numeric characters (A-Z, 0-9)
# Python allows you to assign many values to multiple variables in 1 line
x,y,z = "Orange", "Banana", "Cherry"
print (x)
print (y)
print (z)
# Python allows you to assign one value to multiple variables
x = y = z = "Orange"
print (x)
print (y)
print (z)

# Random number 
import random 
print (random.randrange(1,10))

# Concatenation
# To concatenate or combine two strings you can use the plus operator 
a = "Hello"
b = "Patricia"
c = a + b
print (c)
# Add space between variables
c = a + " " + b
print (c)
# String Format
age = 36 
text = "My name is Patricia, I am " + age
print (txt)
'''
# Python Boolean
# It uses two values True or False, it evaluates any expression to true or to false, Python then evaluates and returns a boolean answer.
print (10 > 9)
print (10 == 9)
print (10 < 9)

# Boolean in a condition (If statement) 
a = 200
b = 33
if b > a:
  print ("b is greater than a")
else:
  print ("a is greater than b")
  # Evaluate values and variables
  # Evaluate a string and a number, example function bool
  print (bool("Hello"))
print (bool(15))
# Operators
# % = modulas
# // = floor division
# + = addition
# - = subtraction
# / = division
# Examples
x = 2
y = 5
# print (x % y)
#print (x // y) #Floor division // rounds the results down to the nearest whole number
print (x ** y) #Same as 2*2*2*2*2