'''
In Python, functions are reusable blocks of code that perform specific tasks. You define them using the def keyword.

'''

def GeometricMean(a,b):
	mean = (a*b)/(a+b)
	print(mean)

GeometricMean(4,5)
GeometricMean(6,7)


def oddOrEven(a):
	if a % 2 == 0:
		print("The provided number is Even")
	else:
		print("The provided number is odd")
oddOrEven(2)
oddOrEven(3)

'''
In Python, pass is a placeholder statement.
It does nothing when executed, but it allows you to write a function or block of code without implementing it yet.

'''
def isGreater(a,b):
	pass


# Function with arguements :

# Required arguements:
def Split(x): # x is required arguement.
	split = str(x) # string conversion
	print(split.split())
Split("This is python programming")

# Default arguements :
def Greet(name="Guest"):
	print("Hello",name,", Good morning!")
Greet("John Doe")

# Keyword arguements :
def Names(fname,lname):
	print("Hi my name is",fname,lname)
Names(lname="Doe",fname="John") # changed order

# Variable length arguements :
# Arbitrary:
def Average(*numbers): # arguements are processed as tuples.
	sum = 0
	for i in numbers :
		sum = sum + i
	print("average is : ", sum/len(numbers))

Average(5,4,5,6)

# Keyword Arbitrary:
def Info(**names): # arguements are processed as Dictionaries.
	print(names)

Info(fname="John",lname="Doe",age=22,work="Python full stack")


'''
Python Functions with return Statements
In Python, the return statement sends a result from a function back to the place where the function was called.

'''

# Return statement :
def Add(a, b):
    return a + b

x = Add(2, 3)
print(x)

# Return statement with multiple values :
def Calculate(a,b):
	return(a+b),(a-b),(a*b)

print("Only calculate :",Calculate(5,15))
addition, subtraction, multiplication = Calculate(10,5)
print("Addition",addition)
print("Subtraction", subtraction)
print("Multiplication", multiplication)
