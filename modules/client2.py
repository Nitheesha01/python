
# Approach 1
# import sys
# sys.path.append("C:/Users/nithe/PycharmProjects/python/day1/modules/package1")
# sys.path.append("C:/Users/nithe/PycharmProjects/python/day1/modules/package1/package2")
#
#
# import module1
# import module2
#
# module1.display()
# module2.show()


# Approach 2
import sys
sys.path.append("C:/Users/nithe/PycharmProjects/python/day1/modules/package1")
sys.path.append("C:/Users/nithe/PycharmProjects/python/day1/modules/package1/package2")

from module1 import *
from module2 import *

display()
show()