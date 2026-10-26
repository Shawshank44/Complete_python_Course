'''
An f-string (formatted string literal) in Python lets you insert variables, expressions, and calculations directly into a string.

'''

# f string working
name = "Priya"
city = "Bengaluru"
marks = 95

print(f"{name} lives in {city}.")
print(f"She scored {marks} marks.")

# using operators in f string
a = 10
b = 5
print(f"Sum = {a + b}")
print(f"Difference = {a - b}")
print(f"Product = {a * b}")
print(f"Division = {a / b}")

# Functions and methods
name = "python"

print(f"Uppercase: {name.upper()}")
print(f"Length: {len(name)}")

'''
Number formatting
Use a colon (:) inside the braces to specify a format.
Syntax	Meaning	Example output
{x:.2f}	2 decimal places	12.35
{x:.3f}	3 decimal places	12.346
{x:10}	Minimum width of 10	Right-aligned
{x:<10}	Left-aligned	Hi
{x:>10}	Right-aligned	Hi
{x:^10}	Center-aligned	Hi
{x:,}	Thousands separator	1,000,000
{x:%}	Percentage format	0.250000%

'''
# Number formatting
price = 1234.5678
print(f"Price: {price:.2f}")
print(f"Price: {price:,.2f}")


# Raw f strings in python
name = "Rahul"
age = 20
print(f"My name is {{name}} and I am {{age}} years old.")
print(f"display curly braces like {{{name}}}")

# Formatting integers
num = 255
print(f"Binary: {num:b}")
print(f"Octal: {num:o}")
print(f"Hexadecimal: {num:x}")
print(f"Hexadecimal: {num:X}")

# Padding numbers with zeros
num = 7
print(f"{num:03}")
print(f"{num:05}")

# Use f-strings with conditions
age = 18
print(f"{'Adult' if age >= 18 else 'Minor'}")

# Display variables with "="
x = 10
y = 20
print(f"{x=}")
print(f"{y=}")
print(f"{x + y=}")
