# This is my Python File

print("hello  this is my first python code")

# take input from user
data = input("Enter name:-")
print(data)

# variable
# variables are used to hold data, value of variable can be change
x = 5
y = "John"
print(x)
print(y)

# x = 4       # x is of type int
x = "Sunday"  # x is now of type str
print(x)

user_age = 30
name = "nitheesha"
email_id = "niteesha.s@gmail.com"

# My name is nitheesha and my email id is niteesha.s@gmail.com

print("My name is " + name + " and my email id is " + email_id)

# Difine 2 variables
first_name = "Nitheesha"
last_name = "Reddy"
print(first_name + " " + last_name)

# Define multiple variables in a line
a, b, c = 10, "Hello", 30
print(a)
print(b)
print(c)

# Assign same values to multiple variables
x = y = z = "apple"
print(x)
print(y)
print(z)

# casting
x = str(5)  # x will be '3'
y = int(8)  # y will be 3
z = float(3)  # z will be 3.0

# get type
A = 5
B = "John"
print(type(A))
print(type(B))

# Define constant here
SCHOOL_CODE = 2121
print(SCHOOL_CODE)
SCHOOL_CODE = 2122

print(SCHOOL_CODE)

x = "Python"
y = "is"
z = "awesome"
print(x, y, z)

"""
x = "Python "
y = "is "
z = "awesome"
print(x + y + z)
"""

# Take Input from user -age, Add 5 to the age and print it
age = input("please enter your age:- ")
age = int(age) + 5
print(age)

# Take integer to string
print("your age is " + str(age))

# Variables that are created outside of a function are known as global variables.
x = "awesome"


def myfunc():
    print("Python is " + x)


myfunc()

x = "awesome"


def myfunc():
    x = "fantastic"
    print("Python is " + x)


myfunc()

print("Python is " + x)

# Data types
# x = 100
# y = 10.5
# s = "welcome"  # s='welcome
# c = 'a'   # c = "a"
# b = True
#
# print(type(x))   # int
# print(type(y))   # float
#
# print(type(s))  # str
# print(type(c))  # str
# print(type(b))  # bool
#
# x = 1234
# print(type(x))  # int
# x = "welcome"
# print(type(x))   # str


# a = 10
# b = 20
# s = "welcome"
#
# print(type(a))
# print(type(b))
# print(type(s))


############# Example 1 ###########
a = 10
b = 10.5
print(a)
print(b)
print(a, b)

########### Example 2 ###############
# a = 10
# b = 20
# c = "welcome"
# a, b, c = 10, 20, "welcome"
# print(a, b)

########### Example 3 ###############
# # a = 100
# # b = 100
# # c = 100
# a = b = c = 100
#
# print(a, b, c)

########### Example 4 ###############

x = 1
y = 2
print(x, y)  # 1 2
y, x = x, y
print(x, y)  # 2 1

########### Example 5 ###############
a = 100
print(a)  # 100
a = "welcome"
print(a)  # welcome

# sting concatenation
a="hello"
b="world"

c=a+" "+b
print(c)
print(a+" "+b)

name=input("Enter your name:-")
phone_number=input("Enter your phone number:-")
print("welcome, your name is " +name+ " and your number is " +phone_number)

#printing data multiple times
print(a*5)

#typecasting data
marks = 60
print("your marks is:-" + str(marks))



#substring
data = "Nitheesha"

print(data[1])

print(data[4:9])

print(data[1:])

print(data[:10])

#length of string
print(len(data))

#string to upper
print(data.upper())

#string to lower
print(data.lower())

#initial character in upper
print(data.capitalize())

#remove spaces from the string
data1="   hello how are you    "

#remove left side spaces
print(len(data1.lstrip()))

#remove right side spaces
print(len(data1.rstrip()))

#to remove all spaces

print(len(data1.strip()))
print(data1.strip())
