import sys
sys.path.append("C:/Users/nithe/PycharmProjects/python/day1/modules/packA")
sys.path.append("C:/Users/nithe/PycharmProjects/python/day1/modules/packB")

# Approach 1
# import emp
# empobj = emp.Employee(101, "John", 600000)
# empobj.displayemp()
#
#
# import stu
# stuobj = stu.Student(2233,"scott",'B')
# stuobj.displaystu()

# Approach 2
from stu import Student
stuobj = Student(2233,"scott",'B')
stuobj.displaystu()

from emp import Employee
empobj = Employee(101, "John", 600000)
empobj.displayemp()