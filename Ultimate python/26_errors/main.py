'''
Error handling in Python is the process of managing runtime errors (exceptions)
so that a program does not crash unexpectedly and can continue executing safely.

Python uses try, except, else, finally, and raise for exception handling.

'''

# Basic error handling - try and except :
try:
	a = int(input("Enter the number you want to see as a table : "))
	for i in range(1,11):
		print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e:
		print("invalid input : ", e)


# Handling specific exceptions - It is better to catch specific exceptions instead of using a general except.
try:
	num = int(input("Enter the number : "))
	result = 10 / num
	print(result)
except ValueError:
	print("Please enter a valid integer.")
except ZeroDivisionError:
	print("Cannot divide by zero.")


# Using else - The else block executes only when no exception occurs.
try:
    num = int(input("Enter a number: "))
    result = 100 / num
except ValueError:
    print("Invalid input.")
except ZeroDivisionError:
    print("Cannot divide by zero.")
else:
    print("Result:", result)

# Using finally - The finally block always executes, whether an exception occurs or not.
def Search(element, list):
	try:
		for i in list:
				if element == i:
					return list.index(element)
		else:
			return False
	except IndexError as i:
			return i
	finally:
		print("Execution completed")
x = [1,2,3,4,5,6]
search = Search(4,x)
print(search)

'''
Execution flow
1. Search(5, x) is called.
2. The loop searches for 5.
3. When it finds 5, Python encounters return list.index(element).
4. Python evaluates the return expression and prepares the return value (4).
5. Before returning to the caller, Python executes the finally block.
6. print("Execution completed") executes.
7. Python completes the pending return and sends 4 to the caller.
8. print(search) prints 4.

finally does not execute before Python evaluates the return expression.
It executes after the return expression is evaluated but before the function completes its return.

'''

# Raising exceptions using raise - The raise keyword allows you to generate exceptions manually.
a = int(input("enter any value between 5 and 9 : "))
if(a < 5 or a > 9):
	raise ValueError("value should be between 5 and 9")

# Custom exceptions - You can create your own exception classes.
class CustomError(Exception):
	pass
user = input("Enter your age : ")
if(user == "quit"):
	print("you quit")
elif(int(user) < 18):
	raise CustomError("You are not eligible to access this")
else:
	print("You are eligible to access this")


# Multiple exceptions in one except block You can handle multiple exceptions using a tuple.
try:
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    print(a / b)
except (ValueError, ZeroDivisionError) as e:
    print("Error:", e)

# Nested try-except You can place one try-except block inside another.
try:
    # Outer try block
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    try:
        # Inner try block
        result = num1 / num2
        print("Result:", result)
    except ZeroDivisionError:
        print("Inner exception: Cannot divide by zero!")
except ValueError:
    print("Outer exception: Please enter valid numbers.")
finally:
    print("Program execution completed.")

# Assert with try-except You can also handle AssertionError using exception handling.
num = -10
try:
    assert num > 0, "Number must be positive"
    print("Valid number")
except AssertionError as e:
    print("Error:", e)
finally:
    print("Execution completed")

# Complete error handling example - This example combines several exception-handling concepts.
def divide_numbers():
    try:
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        result = a / b
    except ValueError:
        print("Error: Please enter valid integers.")

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

    except Exception as e:
        print("Unexpected error:", e)

    else:
        print("Division result:", result)

    finally:
        print("Program execution completed.")

# divide_numbers()


'''
Best practices for Python error handling
1. Always handle specific exceptions whenever possible.
2. Avoid using bare except:.
3. Use finally for cleanup operations.
4. Use with for automatic file and resource management.
5. Use raise when invalid conditions must stop execution.
6. Create custom exceptions for application-specific errors.
7. Log errors instead of relying only on print statements.
8. Don't silently ignore exceptions.
9. Avoid overly broad exception handling.
10. Keep error messages meaningful.

Python error handling cheat sheet :
try - Test risky code
except - Handle exceptions
else - Execute if no exception occurs
finally - Always execute
raise - Generate an exception
as - Store exception details
assert - Check a condition
pass - Do nothing

Common Python exceptions:
ValueError - Invalid value
TypeError - Incorrect data type
ZeroDivisionError - Division by zero
IndexError - Invalid list index
KeyError - Dictionary key not found
NameError - Variable not defined
AttributeError - Invalid object attribute
FileNotFoundError - File does not exist
ImportError - Import failed
ModuleNotFoundError - Module not found
PermissionError - Insufficient file permissions
OSError - Operating system-related error
OverflowError - Numeric operation too large
AssertionError - Assertion condition failed
RuntimeError - General runtime error

'''
