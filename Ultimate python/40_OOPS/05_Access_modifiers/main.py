'''
Access Modifiers in Python
Access modifiers in Python are used to define the accessibility of class variables and methods.
They control how class members can be accessed from inside and outside a class.

Python has three types of access modifiers:
1. Public
2. Protected
3. Private

'''

'''
1. Public Access Modifier
- Public members can be accessed from anywhere.
- They can be accessed inside and outside the class.
- By default, all variables and methods in Python are public.

'''
class Student:
    def __init__(self):
        self.name = "Rahul"

    def display(self):
        print(self.name)

s = Student()
print(s.name)
s.display()


'''
2. Protected Access Modifier
- Protected members are declared using a single underscore (_).
- They are intended to be accessed within the class and its subclasses.
- They can also be accessed from outside the class, but it is not recommended by convention.

'''

class Student:
    def __init__(self):
        self._name = "Rahul"
    def display(self):
        print(self._name)

s = Student()
print(s._name)
s.display()


'''
3. Private Access Modifier
- Private members are declared using a double underscore (__).
- They are intended to be accessed only within the class.
- Python uses a technique called name mangling to make direct access from outside more difficult.
- They cannot be accessed directly using their original name outside the class.

'''
class Student:
    def __init__(self):
        self.__name = "Jack"
    def display(self):
        print(self.__name)

s = Student()
# print(s.__name) # Error Cannot be accessed directly
print(s._Student__name) # this name mangling in python which can be accessed indirectly by modifying the name of the attribute.
s.display()


'''
Difference Between Access Modifiers
Feature - Public - Protected - Private
Symbol - name - _name - __name
Inside class - Yes - Yes - Yes
Outside class - Yes - Yes (by convention) - Not directly
Subclass - Yes - Yes - Not directly by original name
Accessibility	Public - Intended for subclasses - Restricted through name mangling


Important Note
Python does not enforce access modifiers strictly like Java or C++.
- name → Public
- _name → Protected (convention)
- __name → Private (name mangling)
Conclusion: Access modifiers in Python help control the accessibility of variables and methods in a class.
They improve code organization, encapsulation, and data protection.

'''
