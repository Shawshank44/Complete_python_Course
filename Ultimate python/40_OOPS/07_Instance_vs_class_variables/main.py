'''
Class variables vs. Instance variables
The key difference is where the variable belongs and who shares it.

'''
# 1. Instance variables - An instance variable belongs to a specific object (instance) of a class. Each object has its own copy.
class Dog:
    def __init__(self, name):
        self.name = name

dog1 = Dog("Buddy")
dog2 = Dog("Max")
print(dog1.name)
print(dog2.name)

# 2. Class variables - A class variable belongs to the class itself and is shared among all instances of that class.
class Dog:
    species = "Canine"  # Class variable
    def __init__(self, name):
        self.name = name  # Instance variable

dog1 = Dog("Buddy")
dog2 = Dog("Max")
print(dog1.species)  # Canine
print(dog2.species)  # Canine
print(Dog.species)   # Canine


'''
Key differences
Feature - Instance variable - Class variable
Belongs to - Object - Class
Copies - One per instance - Shared across instances
Defined - Usually inside __init__ using self - Inside class body
Accessed using - self.variable - ClassName.variable
Changes	Usually affect one object	Affect shared class-level value

'''
# Example showing the difference
class Employee:
    company = "Google"  # Class variable

    def __init__(self, name, salary):
        self.name = name      # Instance variable
        self.salary = salary  # Instance variable

e1 = Employee("Alice", 50000)
e2 = Employee("Bob", 60000)

e1.salary = 55000
Employee.company = "Microsoft"
print(e1.salary)    # 55000
print(e2.salary)    # 60000
print(e1.company)   # Microsoft
print(e2.company)   # Microsoft


'''
Important Python nuance ⚠️
If you assign a class variable through an instance,
Python typically creates an instance variable that shadows the class variable instead of changing the shared one.

'''
class Counter:
    count = 0

c1 = Counter()
c2 = Counter()
c1.count = 10
print(c1.count)       # 10
print(c2.count)       # 0
print(Counter.count)  # 0

'''
Memory trick:
- Instance variable → My own property.
- Class variable → A property shared by everyone in the class.

'''
