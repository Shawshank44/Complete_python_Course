'''
In Python, dir(), __dict__, and help() are built-in features used for introspection
exploring objects, their attributes, methods, and documentation.

'''

# 1. dir() – List attributes and methods - The dir() function returns a list of names (attributes and methods) available on an object.
class Student:
    def __init__(self, name):
        self.name = name

    def greet(self):
        print("Hello!")

s = Student("John")
print(dir(s))

"""
name → Attribute
greet → Method
__class__ → Special attribute
__dict__ → Stores instance attributes

"""

# 2. __dict__ – Show an object's attributes - __dict__ is an attribute (not a method) that stores an object's attributes in a dictionary.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

s = Student("John", 22)
print(s.__dict__)
print(s.__dict__['name']) # accessing the values.


# 3. help() – Get documentation - The help() function displays documentation about an object, class, function, or module.
help(Student)

# Other examples:
help(list)
help(len)
help(print)

# You can also explore a particular method:
help(str.upper)


'''
Quick comparison
Feature - Purpose - Type
dir() - Lists available attributes and methods - Built-in function
__dict__ - Stores an object's attributes as a dictionary - Attribute
help() - Displays documentation - Built-in function


Remember this simple trick:
- dir() → What is available?
- __dict__ → What data does this object store?
- help() → How does it work?

'''
