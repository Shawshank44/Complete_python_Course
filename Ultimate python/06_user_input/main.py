'''
What is User Input in Python?
User input is the data entered by a user while a program is running.

Python uses the built-in input() function to accept input from the keyboard.

Note : input function always returns the input as a "string". you need typecast the input for int, float etc of values.

'''

a = input("Enter your name : ")
print("My name is", a)

x = input("Enter your first number : ")
y = input("Enter your second number : ")
print(x + y) # without conversion (string concatination)
print(int(x) + int(y)) # with conversion
