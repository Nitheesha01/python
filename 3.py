# Python operators
# Arithmetic Operators
a = 10
b = 3
print("Arithmetic Operators:")
print("a + b =", a + b)  # Addition
print("a - b =", a - b)  # Subtraction
print("a * b =", a * b)  # Multiplication
print("a / b =", a / b)  # Division
print("a % b =", a % b)  # Modulus
print("a ** b =", a ** b)  # Exponentiation
print("a // b =", a // b)  # Floor Division

# Comparison Operators
print("\nComparison Operators:")
print("a == b:", a == b)  # Equal
print("a != b:", a != b)  # Not equal
print("a > b:", a > b)  # Greater
print("a < b:", a < b)  # Less
print("a >= b:", a >= b)  # Greater or equal
print("a <= b:", a <= b)  # Less or equal

# Assignment Operators
print("\nAssignment Operators:")
x = 5
x += 2
print("x += 2:", x)
x *= 3
print("x *= 3:", x)

# Logical Operators
print("\nLogical Operators:")
p = True
q = False
print("p and q:", p and q)
print("p or q:", p or q)
print("not p:", not p)

# Membership Operators
print("\nMembership Operators:")
nums = [1, 2, 3]
print("2 in nums:", 2 in nums)
print("5 not in nums:", 5 not in nums)

# Identity Operators
print("\nIdentity Operators:")
a = [1, 2]
b = a
c = [1, 2]
print("a is b:", a is b)  # True
print("a is c:", a is c)  # False
print("a == c:", a == c)  # True

# Bitwise Operators
print("\nBitwise Operators:")
x = 5  # 0101
y = 3  # 0011
print("x & y:", x & y)
print("x | y:", x | y)
print("x ^ y:", x ^ y)

# Python Lists
mylist = ["apple", "banana", "cherry"]
print(mylist)
# allow duplicates
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
# to find length of a list
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
# list allows String, int and boolean data types
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

print(list1)
print(list2)
print(list3)
list1 = ["abc", 34, True, 40, "male"]
print(list1)
# to find data type
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

# to access the item in a list by using index number, index start with 0
thislist = ["apple", "banana", "cherry"]
print(thislist[1])

# Negative Indexing
# -1 refers to the last item
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])

# to get range
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])  # The search will start at index 2 (included) and end at index 5 (not included)

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])  # ['cherry', 'orange', 'kiwi']
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])  # ['cherry', 'orange', 'kiwi', 'melon', 'mango']

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])  # ['orange', 'kiwi', 'melon']
# Negative indexing means starting from the end of the list(-1).
# This example returns the items from index -4 (included) to index -1 (excluded)
# Remember that the last item has the index -1,

# Check if Item Exists
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
    print("Yes, 'apple' is in the fruits list")
# Change Item Value
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)

# Change a Range of Item Values
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)  # ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']

thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)  # ['apple', 'blackcurrant', 'watermelon', 'cherry']

thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)  # ['apple', 'watermelon']

# Insert Items
# Insert "watermelon" as the third item:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

# Append Items
# To add an item to the end of the list, use the append() method:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)  # ['apple', 'banana', 'cherry', 'orange']

# Insert Items
# To insert a list item at a specified index, use the insert() method.
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)  # ['apple', 'orange', 'banana', 'cherry']

# Extend List
# To append elements from another list to the current list, use the extend() method.
# Add the elements of tropical to thislist:
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)  # ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']

# Add elements of a tuple to a list:
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)  # ['apple', 'banana', 'cherry', 'kiwi', 'orange']

# Remove Specified Item
# Remove "banana":
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

# If there are more than one item with the specified value, Remove the first occurrence of "banana":
thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)  # ['apple', 'cherry', 'banana', 'kiwi']

# The pop() method removes the specified index.
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)  # Remove the second item
# If you do not specify the index, the pop() method removes the last item
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

# The del keyword also removes the specified index:
# Remove the first item:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

# Delete the entire list:
thislist = ["apple", "banana", "cherry"]
del thislist

# Clear the list content:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)  # []

# Print all items in the list, one by one:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)

# Print all items by referring to their index number:
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

# Print all items, using a while loop
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist)  # it will append all items which contain letter a

# one line code
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
# newlist = [expression for item in iterable if condition == True]

# Sort the list alphabetically:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

# Sort the list numerically:
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

# To sort descending, use the keyword argument reverse = True:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

# if you want a case-insensitive sort function, use str.lower as a key function:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

# The reverse() method reverses the current sorting order of the elements.
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

# Make a copy of a list with the copy() method:
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

# another way to copt by using list with the list() method:
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)

# another way by using slice
thislist = ["apple", "banana", "cherry"]
mylist = thislist[:2]
print(mylist)

# Join two list:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

# Append list2 into list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
for x in list2:
  list1.append(x)
print(list1)

# Use the extend() method to add list2 at the end of list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)
