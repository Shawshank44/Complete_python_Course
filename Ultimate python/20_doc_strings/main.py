'''
In Python, complete docstrings and PEP 8 compliance mean documenting your code clearly
and following Python's standard style guidelines so it is readable, consistent, and maintainable.

'''

def square(n):
	'''
	This is a doc string which explains what a function can do.
	this function takes a number n, returns the square of n

	'''
	return(n**2)

print(square(5))
print(square.__doc__) # loads the doc string


# PEP 8 (python enhancement program)
'''
PEP 8 guidelines
PEP 8 is Python's official style guide. The key conventions are:
Element	Convention	Example
Variables	snake_case	total_price
Functions	snake_case	calculate_total()
Classes	PascalCase	BankAccount
Constants	UPPER_SNAKE_CASE	MAX_RETRIES
Indentation	4 spaces	Standard block indentation
Line length	Usually up to 79 characters	Break long lines logically
Imports	At the top of the file	Standard library, third-party, local
Strings	Consistent quote style	"Hello"
Blank lines	Two around top-level functions and classes	Separate definitions clearly

'''
