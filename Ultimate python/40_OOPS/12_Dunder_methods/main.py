'''
Dunder methods (short for Double Underscore methods) are special methods whose names begin and end with double underscores (__).
They are also called magic methods because Python automatically calls them in certain situations.

Common dunder methods in Python
Dunder method	Purpose
__init__()	Initializes an object
__str__()	Returns a user-friendly string
__repr__()	Returns a developer-friendly representation
__len__()	Defines behavior of len()
__add__()	Defines behavior of +
__sub__()	Defines behavior of -
__mul__()	Defines behavior of *
__eq__()	Defines behavior of ==
__lt__()	Defines behavior of <
__del__()	Called when an object is finalized

'''
# Example __init__() is a dunder method. Python automatically calls it when you create an object.
class Student:
    def __init__(self, name):
        self.name = name
    def info(self):
        print(self.name)

s1 = Student("Rahul")
s1.info()

# Example of __str__() :
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} is {self.age} years old"

s1 = Student("Rahul", 30)
print(s1)


# Example of __add__() - We can customize the (+) operator using __add__().
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + other.value

n1 = Number(10)
n2 = Number(20)
print(n1 + n2)


# Example of __len__()
class MyList:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

obj = MyList([10, 20, 30, 40])
print(len(obj))


# Example __repr__() — Developer-friendly representation - This method defines the official or debugging representation of an object.
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return f"Student(name={self.name!r}, age={self.age!r})"

s1 = Student("Rahul", 22)
print(repr(s1))

# Difference between __str__() and __repr__()
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name}, age {self.age}"
    def __repr__(self):
        return f"Student({self.name!r}, {self.age!r})"

s1 = Student("Rahul", 22)
print(str(s1))
print(repr(s1))

# Example __eq__() — Customize equality (==)
# By default, two separate objects are generally considered unequal unless their equality behavior is customized.
# With __eq__(), we decide when two objects should be considered equal.
class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name

    def __eq__(self, other):
        if not isinstance(other, Student):
            return NotImplemented

        return self.student_id == other.student_id

s1 = Student(101, "Rahul")
s2 = Student(101, "Amit")
s3 = Student(102, "Rahul")
print(s1 == s2)
print(s1 == s3)

'''
Other comparison dunder methods
Method - Operator
__eq__() - ==
__ne__() - !=
__lt__() - <
__gt__() - >
__le__() - <=
__ge__() - >=

'''

# Example __call__() — Make an object behave like a function - This is one of the most interesting dunder methods.
class Greeter:
    def __call__(self, name):
        print(f"Hello, {name}!")

greet = Greeter()
greet("Rahul")


'''
Focus especially on __init__(), __str__(), __repr__(), __add__(), __len__(), and __eq__().
These are useful dunder methods to understand when learning Python OOP.

'''
