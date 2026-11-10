'''
How Imports Work in Python
In Python, imports allow you to use code (functions, classes, variables, etc.) written in another Python file or library without rewriting it.

'''
# 1. imports
import math # Import the entire module
# import math as m # Import using an alias
# from math import sqrt, pi # Import specific functions or variables
# from math import * # Import everything

# 2. importing custom functions and variables from another module
# from test_imp import Welcome, constant
import test_imp as ti

# 3. Lazy imports - Python 3.15 introduces Explicit Lazy Imports (PEP 810),
# a new language feature that allows you to postpone importing modules until you actually use them.
# lazy import random as rn
lazy from random import randint



sqrt = math.sqrt(9) * math.pi
print(sqrt)

# The dir() function in Python is a built-in function used to find the attributes and methods available in an object.
print(dir(math))

# Using custom imported functions.
print(ti.Welcome())
print(ti.constant)

# using the random function via lazy imports
print(randint(1,100))

