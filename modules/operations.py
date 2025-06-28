# Approach 1
from modules import calculator

calculator.sum(100, 200)
calculator.mul(4, 5)

# Approach 2
from modules.calculator import sum, mul

sum(20, 30)
mul(50, 4)

# Approach 3
from modules.calculator import *

sum(20, 30)
mul(50, 4)
