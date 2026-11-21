'''
Python Decorators
A decorator in Python is a function that modifies or extends the behavior of another function without changing its original code.

In simple words, a decorator allows you to add extra functionality to an existing function.

'''

from functools import wraps

# 1. Decorator example:
def myDecorator(fx):
	def wrapper():
		print("Before function execution")
		fx()
		print("After function execution")
	return wrapper

@myDecorator
def greet():
	print("Hi, This is greet function")

greet()

'''
How does it work?
Let's understand step by step:
1. my_decorator accepts another function as an argument.
2. wrapper() adds extra functionality.
3. func() executes the original function.
4. return wrapper returns the modified function.
5. @my_decorator applies the decorator to greet().

'''

# 2. Decorators with arguments - What if the original function accepts arguments?
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Function started")
        result = func(*args, **kwargs)
        print("Function completed")
        return result
    return wrapper

@my_decorator
def add(a, b, c):
    return a + b + c
print(add(10, 20, 30))


# 3. passing arguments inside a decorator.
def my_decorator(message, count):
    def decorator(func):
        @wraps(func) # @wraps(func) preserves the original function's identity and metadata after decorating it.
        def wrapper(*args, **kwargs):
            for i in range(count):
                print(message)
            return func(*args, **kwargs)
        return wrapper
    return decorator

@my_decorator("Python is awesome!", 3)
def greeting():
    """This function prints a greeting."""
    print("Hello!")

greeting()
print(greeting.__name__)
print(greeting.__doc__)

'''
Here:
- *args handles positional arguments.
- **kwargs handles keyword arguments.
- result stores the original function's return value.

'''

'''
Types of built-in decorators
Python provides several built-in decorators.
Decorator	Purpose
@staticmethod	Defines a method that doesn't receive self or cls automatically
@classmethod	Defines a method that receives the class as its first argument
@property	Allows a method to be accessed like an attribute
@functools.wraps	Preserves function metadata

'''

'''
In Python, decorators are commonly used inside classes to define methods and control how they behave.
There are 4 important decorators you should understand when working with classes:
1. @staticmethod
2. @classmethod
3. @property
4. Custom decorators applied to class methods

'''

'''
1. @staticmethod
A static method does not receive self or cls automatically.
Use it when a method does not need to access instance or class data.

'''
class Math:
      @staticmethod
      def add(a,b):
            print(a+b)
Math.add(1,2)


'''
2. @classmethod
A class method receives the class itself as its first argument (cls).
Use it when you want to access or modify class-level variables.

'''
class Employee:
    company = "Google"
    @classmethod
    def change_company(cls, name):
        cls.company = name

    @classmethod
    def display_company(cls):
        print(cls.company)

Employee.display_company()
Employee.change_company("Microsoft")
Employee.display_company()


'''
3. @property
The @property decorator allows you to access a method like an attribute.

'''
class Employee:
    def __init__(self, name):
        self._name = name
    @property
    def name(self):
        return self._name

emp = Employee("John")
print(emp.name)


'''
4. Custom decorator inside a class
This is particularly important because it connects to the decorator you learned earlier.
Let's create a custom decorator and apply it to a class method.

'''
def check_login(fx):
     def wrapper(self, *args, **kwargs):
          if not self.is_logged_in:
            print("please login first")
            return
          return fx(self, *args, **kwargs)
     return wrapper

class Bank:
    def __init__(self):
        self.is_logged_in = False
        self.balance = 10000
    @check_login
    def withdraw(self, amount):
        self.balance -= amount
        print("Remaining balance:", self.balance)

account = Bank()
account.withdraw(2000)
account.is_logged_in = True
account.withdraw(2000)


'''
5. Difference between class decorators
Decorator	First argument - Main purpose
@staticmethod	None automatically - Independent utility methods
@classmethod - cls	Access class-level data
@property	self - Access methods like attributes
Custom decorator - Depends on method binding	Add reusable functionality

'''
