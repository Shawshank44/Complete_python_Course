'''
In Python, completing class methods means implementing the functions defined inside a class so that they perform the required operations.

A good way to understand all five types of methods is through one practical example: a Bank Account class.
We'll use a single class to see how __init__(), instance methods, @classmethod, @staticmethod, and __str__() work together.

'''
class BankAccount:
    # Class variable (shared by all accounts)
    bank_name = "ABC Bank"

    # 1. Constructor
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    # 2. Instance method
    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            return "Insufficient balance"

    # 3. Class method
    @classmethod
    def change_bank_name(cls, new_name):
        cls.bank_name = new_name

    # 4. Static method
    @staticmethod
    def is_valid_amount(amount):
        return amount > 0

    # 5. String method
    def __str__(self):
        return f"Account holder: {self.name}, Balance: ₹{self.balance}"


acc1 = BankAccount("John Doe", 20000)
acc1.deposit(20000)
acc1.withdraw(10)

BankAccount.change_bank_name("XYZ Bank") # Class method
print(acc1.is_valid_amount(500)) # static method


print(acc1) # prints the def __str__(self) method

print(BankAccount.bank_name) # changes bank name


# class methods as Alternative constructors:
'''
An alternative constructor is a method that provides another way to create an object besides the regular __init__() constructor.
In Python, we typically implement alternative constructors using the @classmethod decorator.

'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def from_string(cls, data):
        name, age = data.split("-")
        return cls(name, int(age)) # returning class instance

# Regular constructor
p1 = Person("alice", 29)

# Alternative constructor
p2 = Person.from_string("Bob-30")
print(p1.name, p1.age)
print(p2.name, p2.age)


'''
How does it work?
Let's understand the important parts:
- @classmethod: Makes the method a class method.
- cls: Refers to the class itself, similar to how self refers to an instance.
- from_string(): Takes a string and extracts the required attributes.
- return cls(name, int(age)): Creates and returns a new object using the class constructor.

Common use cases
Alternative constructors are useful when you want to create objects from different data formats.
Method	Purpose
from_string()	Create an object from a string
from_dict()	Create an object from a dictionary
from_json()	Create an object from JSON
from_file()	Create an object using file data


Key takeaway :
A class method can act as an alternative constructor because it can create and return a new instance of its class using cls().
Remember:
- __init__() initializes an object.
- @classmethod receives the class as its first argument.
- cls() creates an instance of the class.
- Alternative constructors provide convenient ways to create objects from different inputs.

'''
