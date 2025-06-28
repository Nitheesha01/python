# Example 1
class MyClass:
    def myfun(self):
        pass

    def display(self):
        print("Nitheesha")


mc1 = MyClass()
mc1.myfun()
mc1.display()


# Example 2
class MyClass:
    def m1(self):
        print("This is instance method")

    @staticmethod
    def m2(self, num):
        print(num)


mc = MyClass()
mc.m1()
mc.m2(100, 200)  # 100 200

MyClass.m2(10, 20)


# ex 3
class MyClass:
    a, b = 10, 20  # class variables

    def add(self):
        print(self.a + self.b)

    def mul(self):
        print(self.a * self.b)


mc = MyClass()
mc.add()  # 30
mc.mul()  # 200

# ex 4

i, j = 15, 25  # global variables


class MyClass:
    a, b = 10, 20  # class variables

    def add(self, x, y):
        print(x + y)  # x,y are local variables
        print(self.a + self.b)  # a,b are class variables
        print(i + j)  # i,j are global variables


mc = MyClass()
mc.add(40, 50)

# ex 5

a, b = 10, 20  # global variables


class MyClass:
    a, b = 15, 25

    def add(self, a, b):
        print(a + b)
        print(self.a + self.b)
        print(globals()['a'] + globals()['b'])


mc = MyClass()
mc.add(30, 40)


# ex 6
# one class can have multiple objects
class MyClass:
    def display(self, name):
        print("this is display method........")
        print(name)


obj1 = MyClass()
obj1.display("nitheesha")

obj2 = MyClass()
obj2.display("Manvika")


# ex 7 constructor
class MyClass:
    def __init__(self):
        print("this is constructor")

    def m1(self):
        print("hello")

    def m2(self, a, b):
        return (a + b)


mc = MyClass()  # invoke constructor automatically
mc.m1()  # method we have to call explicitly by using object
print(mc.m2(10, 20))  # 30


# ex 8
class MyClass:
    name = "nith"

    def __init__(self, name):  # constructor expecting one parameter
        print(name)
        print(self.name)


mc = MyClass("Nitheesha")  # passing parameter to the constructor


# ex 9
# req: exp
# constructor : eid, ename, sal
# display(): print eid, ename &sal
class Emp:

    def __init__(self, eid, ename, sal):
        self.eid = eid
        self.ename = ename
        self.sal = sal

    def display(self):
        print(self.eid, self.ename, self.sal)


e1 = Emp(101, "Nith", 50000)
e1.display()

e2 = Emp(102, "Nitheesha", 80000)
e2.display()


# Inheritance
# Example 1
class A:
    def m1(self):
        print("this is m1 method from classA")


class B(A):
    def m2(self):
        print("this is m2 method from class B")


bobj = B()
bobj.m1()
bobj.m2()


# Example 2 : single inheritance
class A:
    x, y = 10, 20

    def m1(self):
        print(self.x + self.y)


class B(A):
    a, b = 200, 100

    def m2(self):
        print(self.a - self.b)


bobj = B()
bobj.m1()  # 30
bobj.m2()  # 100


# Example 3 : MUltilevel inheritance
class A:
    x, y = 10, 20

    def m1(self):
        print(self.x + self.y)


class B(A):
    a, b = 200, 100

    def m2(self):
        print(self.a - self.b)


class C(B):
    i, j = 5, 2

    def m3(self):
        print(self.i * self.j)


cobj = C()
cobj.m1()  # 30
cobj.m2()  # 100
cobj.m3()  # 10


# example 4: hierarchy inheritance
class A:
    x, y = 10, 20

    def m1(self):
        print(self.x + self.y)


class B(A):
    a, b = 200, 100

    def m2(self):
        print(self.a - self.b)


class C(A):
    i, j = 5, 2

    def m3(self):
        print(self.i * self.j)


bobj = B()
bobj.m1()  # 30
bobj.m2()  # 100

cobj = C()
cobj.m1()  # 30
cobj.m3()  # 10


# example 5 : Multiple inheritance
class A:
    x, y = 10, 20

    def m1(self):
        print(self.x + self.y)


class B:
    a, b = 200, 100

    def m2(self):
        print(self.a - self.b)


class C(A, B):
    i, j = 5, 2

    def m3(self):
        print(self.i * self.j)


cobj = C()
cobj.m1()  # 30
cobj.m2()  # 100
cobj.m3()  # 10


# example 6 : calling parent class method using child class(super())
class A:
    def m1(self):
        print("This is m1 method from class A")


class B(A):
    def m1(self):
        print("This is m1 method from class B")
        super().m1()


bobj = B()
bobj.m1()  # This is m1 method from class B


# without super(), it will print "This is m1 method from class A"


# Example 7
class A:
    a, b = 10, 20


class B(A):
    i, j = 100, 200

    def m(self, x, y):
        print(x + y)  # local variables
        print(self.i + self.j)  # class variables
        print(self.a + self.b)  # class variables


bobj = B()
bobj.m(100, 200)


# Example 8 : overriding variables
class Parent:
    name = "Nitheesh"


class Child(Parent):
    name = "Manvika"  # overriding the variable value

    def test(self):
        print(super().name)


cobj = Child()
print(cobj.name)
cobj.test()


# Example 9 : overriding methods
class Bank:
    def rateOfInterest(self):
        return 0


class XBank(Bank):
    def rateOfInterest(self):
        return 10


class YBank(Bank):
    def rateOfInterest(self):
        return 12


objx = XBank()
print(objx.rateOfInterest())  # 10

objy = YBank()
print(objy.rateOfInterest())  # 12


# Example 10 : overloading (polymorphism)
class Human:
    def sayhello(self, name=None):
        if name is not None:
            print("Hello " + name)
        else:
            print("Hello")


h = Human()
h.sayhello("Nitheesha")
h.sayhello()


# Example 11 : overloading (polymorphism)
class Calculation:
    def add(self, a=0, b=0, c=0):
        print(a + b + c)


calobj = Calculation()
calobj.add()  # 0
calobj.add(10, 20)  # 30
calobj.add(100, 200, 300)  # 600


class Circle:
    def area(self):
        print("Area of circle = π * r * r")


class Square:
    def area(self):
        print("Area of square = side * side")


# Polymorphism in action
def print_area(shape):
    shape.area()


c = Circle()
s = Square()

print_area(c)  # Calls Circle's area
print_area(s)  # Calls Square's area


class Developer:
    def work(self):
        print("Writing code")


class Designer:
    def work(self):
        print("Designing UI")


employees = [Developer(), Designer()]

for emp in employees:
    emp.work()  # Same method, different results


class Animal:
    def sound(self):
        print("Animal makes sound")


class Dog(Animal):
    def sound(self):
        print("Dog barks")


class Cat(Animal):
    def sound(self):
        print("Cat meows")


animals = [Dog(), Cat()]

for a in animals:
    a.sound()  # Polymorphic behavior


# Different classes with the same method:

class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive!")


class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail!")


class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly!")


car1 = Car("Ford", "Mustang")  # Create a Car object
boat1 = Boat("Ibiza", "Touring 20")  # Create a Boat object
plane1 = Plane("Boeing", "747")  # Create a Plane object

for x in (car1, boat1, plane1):
    x.move()


# Create a class called Vehicle and make Car, Boat, Plane child classes of Vehicle:

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Move!")


class Car(Vehicle):
    pass


class Boat(Vehicle):
    def move(self):
        print("Sail!")


class Plane(Vehicle):
    def move(self):
        print("Fly!")


car1 = Car("Ford", "Mustang")  # Create a Car object
boat1 = Boat("Ibiza", "Touring 20")  # Create a Boat object
plane1 = Plane("Boeing", "747")  # Create a Plane object

for x in (car1, boat1, plane1):
    print(x.brand)
    print(x.model)
    x.move()

# A variable created inside a function is available inside that function:
# local scope
def myfunc():
  x = 300
  print(x)

myfunc()

# The local variable can be accessed from a function within the function:
# Function Inside Function
def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

# A variable created outside of a function is global and can be used by anyone:
# Global Scope
x = 300

def myfunc():
  print(x)

myfunc()

print(x)

# The function will print the local x, and then the code will print the global x:
# Naming Variables
x = 300

def myfunc():
  x = 200
  print(x)

myfunc()

print(x)

# If you use the global keyword, the variable belongs to the global scope:
# Global Keyword
def myfunc():
  global x
  x = 300

myfunc()

print(x)

# To change the value of a global variable inside a function, refer to the variable by using the global keyword:
x = 300

def myfunc():
  global x
  x = 200

myfunc()

print(x)