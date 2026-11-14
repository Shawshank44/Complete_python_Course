'''
In Python, local variables and global variables are two types of variables based on where they are declared and where they can be accessed.

'''

# 1. Local Variable - A local variable is a variable declared inside a function. It can only be accessed within that function.
def my_function():
    x = 10  # Local variable
    print(x)
my_function()

# 2. Global Variable - A global variable is a variable declared outside all functions. It can be accessed throughout the program.
y = 20  # Global variable
def my_func():
    print(y)
my_func()
print(y)

# 3. Using the global Keyword - If you want to modify a global variable inside a function, use the global keyword.
z = 10
def change_value():
    global z
    z = 50
change_value()
print(z)


'''
Difference Between Local and Global Variables
Local Variable - Global Variable
Declared inside a function. - Declared outside a function.
Accessible only inside its function. - Accessible throughout the module.
Created when the function executes. - Usually created when the module runs.
Cannot normally be accessed outside the function. - Can be accessed inside and outside functions.

'''
