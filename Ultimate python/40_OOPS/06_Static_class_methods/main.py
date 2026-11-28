'''
Static Methods in Python
A static method in Python is a method that belongs to a class but does not depend on the instance (self) or the class (cls).

It is used when a function logically belongs to a class but doesn't need to access instance variables or class variables.

Why Do We Use Static Methods?
Static methods are useful when:
- A function is related to a class logically.
- It doesn't need instance variables.
- It doesn't need class variables.
- We want to organize utility/helper functions inside a class.
- We don't want to unnecessarily create objects to call a function.

'''

# 1. Syntax - We use the @staticmethod decorator to define a static method.
class Math:
	@staticmethod
	def add(a,b):
		return a+b

print(Math.add(12,13))

'''
Here:
- @staticmethod makes the method static.
- add() doesn't take self or cls.
- We can call it directly using the class name.

'''

# 2. Calling a Static Method Using an Object - We can also call a static method using an object.
class Calculator:
	@staticmethod
	def multiply(a,b):
		return a * b

c = Calculator()
print(c.multiply(30,30))


'''
Class Method in Python
A class method is a method that belongs to the class itself rather than a particular object (instance).
It is used to access or modify class variables. We define it using the @classmethod decorator.
A class method takes cls as its first parameter, which refers to the class itself.

'''
# 1. Syntax of a Class Method
class Student:
    school = "ABC School"
    @classmethod
    def display(cls):
        print(cls.school)

Student.display()

# 2. Class Method Accessing Class Variables
class Employee:
    company = "Google"
    employees = 100

    @classmethod
    def display(cls):
        print("Company:", cls.company)
        print("Employees:", cls.employees)

Employee.display()


'''
A static method cannot automatically access instance variables because it doesn't receive self.

3. Static Method vs Instance Method vs Class Method
Feature	Instance Method - Class Method - Static Method
Decorator	None - @classmethod - @staticmethod
First parameter - self - cls - None
Access instance data - Yes - No (directly) - No
Access class data - Yes - Yes - No (directly)
Called using class - Usually needs object - Yes - Yes
Called using object - Yes - Yes - Yes



Remember this simple rule:
- self → Instance method → Works with object data.
- cls → Class method → Works with class data.
- No self, no cls → Static method → Utility function.

'''
# Example of all three :
class Student:
    school = "ABC School"

    def instance_method(self):
        return "Instance method"

    @classmethod
    def class_method(cls):
        return cls.school

    @staticmethod
    def static_method():
        return "Static method"


s = Student()
print(s.instance_method())
print(Student.class_method())
print(Student.static_method())
