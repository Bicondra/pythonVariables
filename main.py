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