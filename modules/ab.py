# Approach 1 import modulename
import a
import b

obj1=a.Animal()
obj1.display()

obj2=b.Bird()
obj2.display()

# Approach 2 from modulename import functions, classes
from a import Animal
from b import Bird

obj1=Animal()
obj1.display()

obj2=Bird()
obj2.display()