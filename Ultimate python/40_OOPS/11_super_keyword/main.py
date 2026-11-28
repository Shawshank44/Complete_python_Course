'''
In Python, the super() keyword (technically, a built-in function) is used to call methods of a parent class from a child class.
It is commonly used in inheritance.

'''
# Example Using super() with parameters
class Parent:
    def __init__(self, name):
        self.name = name
    def parentMethod(self, name):
        print("This is parent method", name)

class Child(Parent):
    def __init__(self, name, age):
        super().__init__(name) # implementation of super keyword
        self.age = age
    def childMethod(self):
        super().parentMethod(self.name)
        print("This is child method", self.name, self.age)

obj = Child("Rahul", 22)

obj.childMethod()


'''
What is the difference between super() and self?
self - super()
Refers to the current object. - Provides access to the next class in the MRO.
Accesses current class methods and attributes. - Calls inherited methods through the MRO.
Used with instance methods. - Commonly used in inheritance.


Why do we use super()?
1. To access parent class methods.
2. To call the parent class constructor.
3. To avoid directly referring to the parent class name.
4. To support multiple inheritance through Python's Method Resolution Order (MRO).

Remember:
- self → Current object.
- super() → Next class in the Method Resolution Order.

'''
