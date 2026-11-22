'''
Getters and Setters in Python
In Python, getters and setters are methods used to access and modify the values of class attributes while maintaining control over how those values are accessed or changed.

They are commonly used in Encapsulation, one of the four pillars of Object-Oriented Programming (OOP).
1. What is a Getter?
A getter is a method used to retrieve or read the value of a private attribute.
2. What is a Setter?
A setter is a method used to modify or update the value of a private attribute.

'''

class Student:
	def __init__(self,value):
		self.value = value

	@property # Getter
	def name(self):
		return self.value

	@name.setter # Setter
	def name(self,value):
		self.value = value

s1 = Student("John Doe")
print(s1.name) # Getter

s1.name = "Jack Doe" # Setter
print(s1.name)

'''
Notice that we use:
- @property to define a getter.
- @name.setter to define a setter.
- s1.name to access the attribute.
- s1.name = "Jack Doe" to update the attribute.

Difference Between Getter and Setter
Getter - Setter
Reads an attribute - Updates an attribute
Returns a value - Accepts a value
Uses @property - Uses @attribute.setter
Does not modify the value - Can modify the value
Used for retrieving data - Used for updating data


Why Do We Use Getters and Setters?
1. Encapsulation: Protects internal class attributes.
2. Data Validation: Prevents invalid values.
3. Data Security: Controls access to attributes.
4. Maintainability: Makes it easier to change internal implementation.
5. Controlled Access: Allows specific rules when reading or updating values.

What is the difference between normal methods and getters and setters in Python?

Answer: Normal methods perform general operations, whereas getters and setters specifically control how class attributes are accessed and modified.
In Python, the @property decorator allows us to implement getters and setters using normal attribute syntax.

Remember: Python does not require getters and setters for every attribute.
We can directly access public attributes. Getters and setters are especially useful when validation or controlled access is required.

'''
