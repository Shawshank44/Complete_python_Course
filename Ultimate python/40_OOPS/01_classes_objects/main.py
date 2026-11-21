'''
Classes and Objects in Python
In Python, classes and objects are important concepts of Object-Oriented Programming (OOP).

1. What is a Class?
A class is a blueprint or template used to create objects.

It defines:
- Attributes (variables)
- Methods (functions)

'''
class Person:
	name = "John Doe"
	occupation = "Software Developer"
	netWorth = 10
	def info(self):
		print(f"{self.name} is a {self.occupation}")
'''
Here:
- Person is the class name.
- name, occupation, and netWorth are attributes.
- info() is a method.
- self refers to the current object.

'''


'''
2. What is an Object?
An object is an instance of a class.
An object is created using the class name.

'''
a = Person() # Creating an object
a.name = "Jack Doe"
a.occupation = "Tester"
a.info() # Calling the method

b = Person()
b.name = "Aaron benson"
b.occupation = "System tech"
b.info()

''' Here, a and b are object of the Student class. '''

'''
3. Constructor in Python
A constructor is a special method that is automatically called when an object is created.
Python uses __init__() as a constructor.

'''
class Student:
	def __init__(self, name, age):
		self.name = name
		self.age = age
	def display(self):
		return f"{self.name} is {self.age} years old"

s1 = Student("Navin", 18)
print(s1.display())
print(s1.name) # Instance variables belong to individual objects.


'''
Important points to remember:
1. Class is a blueprint.
2. Object is an instance of a class.
3. class keyword is used to create a class.
4. __init__() is the constructor.
5. self refers to the current object.
6. Methods are functions defined inside a class.

'''
