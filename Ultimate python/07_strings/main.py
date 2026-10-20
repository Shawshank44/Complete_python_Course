'''
Strings in Python – Complete Guide
A string in Python is a sequence of characters enclosed in single quotes, double quotes, or triple quotes.
Strings are used to store text such as names, sentences, addresses, and messages.

'''

# Single quotes
a = 'Hello'

# Double quotes
b = "Python"

# Triple quotes
c = '''Welcome to Python'''

d = """This is a
multiline string."""

e = 'This is "enclosed"'

print(a)
print(b)
print(c)
print(d)
print(e)


# String indexing
s = "PYTHON"

# positive indexing
print(s[0])  # P
print(s[1])  # Y
print(s[5])  # N

# negative indexing
print(s[-1])  # N
print(s[-2])  # O
print(s[-6])  # P


# String slicing string[start:stop:step]
print(s[-1:-4:-1]) # NOH
print(s[0:3])   # PYT
print(s[2:5])   # THO
print(s[:4])    # PYTH
print(s[2:])    # THON
print(s[:])     # PYTHON
print(s[::2])   # PTO
print(s[::-1])  # NOHTYP
print(s[-1:len(s)-3]) # by default python adds the len function.
print(s[-4:-2])

# looping strings (iterating the strings)
for char in s:
	print(char)


# finding the length of the string
print(len(s))


# String Operators in Python
print("Py" + "thon")          # Python
print("Hi" * 3)               # HiHiHi
print("P" in "Python")        # True
print("z" not in "Python")    # True
print("abc" == "abc")         # True
print("abc" != "xyz")         # True
