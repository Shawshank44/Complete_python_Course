'''
Type Casting in Python – Complete Guide
1. What is Type Casting?
Type casting in Python is the process of converting a value from one data type to another.

'''


# Explicit typecasting
a = int(10.8)
print(a)  # 10

b = int("25")
print(b)  # 25

c = int(True)
print(c)  # 1

d = int(False)
print(d)  # 2


# Implicit type casting
a = 10       # int
b = 2.5      # float

c = (a + b)

print(c)         # 12.5
print(type(c))   # <class 'float'>
