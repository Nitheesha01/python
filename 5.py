# Print i as long as i is less than 6:
i = 1
while i < 6:
    print(i)
    i += 1

# Exit the loop when i is 3:
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# Continue to the next iteration if i is 3
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
print(i)

# Print a message once the condition is false:
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")

# for loop
# to print each fruit in the list
fruits = ["apple", "banana", "orange"]
for i in fruits:
    print(i)

# loop through letter
for x in "Nitheeesha":
    print(x)

# break statement
# Exit the loop when i is "banana":
fruits = ["apple", "banana", "orange"]
for i in fruits:
    print(i)
    if i == "banana":
        break

# continue statement
print("continue statement")
fruits = ["apple", "banana", "mango"]
for i in fruits:
    if i == "banana":
        continue
    print(i)

# by using range() function
for i in range(5):
    print(i)

for i in range(4, 8):
    print(i)

for i in range(1, 20, 2):
    print(i)

# Print all numbers from 0 to 5, and print a message when the loop has ended:
for x in range(6):
    print(x)
else:
    print("Finally finished!")

# If the loop breaks, the else block is not executed.
for x in range(6):
    if x == 3: break
    print(x)
else:
    print("Finally finished!")

# nested loop
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)

for i in range(1, 4):  # Outer loop (1 to 3)
    for j in range(1, 6):  # Inner loop (1 to 5)
        print(f"{i} x {j} = {i * j}")
    print("-----")  # Separator between tables

# having an empty for loop like this, would raise an error without the pass statement
for x in [0, 1, 2]:
    pass


# python functions
def my_function():
    print("Hello from a function")


my_function()


# function using arguments
def my_function(fname):
    print(fname + " Refsnes")


my_function("Emil")
my_function("Tobias")
my_function("Linus")


def my_function(fname, lname):
    print(fname + " " + lname)


my_function("nitheesha", "Reddy")


# If the number of arguments is unknown, add a * before the parameter name:

def my_function(*kids):
    print("The youngest child is " + kids[2])


my_function("Emil", "Tobias", "Linus")


# by using key value syntax
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)


my_function(child1="Emil", child2="Tobias", child3="Linus")


def my_function(country="Norway"):
    print("I am from " + country)


my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")


# Passing a List as an Argument
def my_function(food):
    for fruits in food:
        print(fruits)


fruits = ["apple", "banana", "cherry"]

my_function(fruits)


# using return statement
def my_function(x):
    return 5 * x


print(my_function(3))
print(my_function(5))
print(my_function(9))


def my_function(x):
    print(x)


my_function(x=3)


# Recursion Example
def tri_recursion(k):
    if (k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result


print("Recursion Example Results:")
tri_recursion(6)

# using array
cars = ["Ford", "Volvo", "BMW"]
n = cars[0]
print(n)

# to modifies
cars = ["Ford", "Volvo", "BMW"]
cars[0] = "Toyota"
print(cars)


# to get the length of an array
cars = ["Ford", "Volvo", "BMW"]
x = len(cars)
print(x)

 # Looping Array Elements
cars = ["Ford", "Volvo", "BMW"]
for x in cars:
  print(x)

# to add new element
cars = ["Ford", "Volvo", "BMW"]
cars.append("Honda")
print(cars)

