'''
In Python, tuples are ordered collections of items that cannot be changed after creation.
If you mean complete tuples in Python, here are the basics.

'''
# Single-element tuple.
t = (5,) # without "," python will consider this as a type "int"
print(type(t))  # <class 'tuple'>

# Multiple element tuple.
tup = (1,5,6,67,86, 467)
print(type(tup), tup)

# Tuple without parentheses.
t = 10, 20, 30
print(type(t),t)

# Converting a list into a tuple
numbers = [1, 2, 3]
t = tuple(numbers)
print(t)  # (1, 2, 3)

# Positive indexing
t = (10, 20, 30, 40, 50)
print(t[0])  # 10
print(t[1])  # 20
print(t[2])  # 30
print(t[3])  # 40
print(t[4])  # 50

# Negative indexing
t = (10, 20, 30, 40, 50)
print(t[-1])  # 50
print(t[-2])  # 40
print(t[-3])  # 30
print(t[-4])  # 20
print(t[-5])  # 10

# Slicing in tuple tuple[start : stop : Jumpindex] returns a new sliced tuple.
t = (10, 20, 30, 40, 50, 60)
print(t[1:4])     # Positive slicing
print(t[-4:-1])   # Negative slicing
print(t[1:-1])    # Positive start, negative stop
print(t[-1:-5:-1]) # Negative slicing in reverse


# validating tuple elements using "in" keyword
names = ("ram", "ravi", "rishi", "raghav")
if "ram" in names:
	print("yes it exists")
else:
	print("no does not exists")


# iteration over tuple
elements = ("John Doe", 22, 5.5, True)
for e in elements:
	print(e)

'''
We cannot directly manupulate tuples. If we want to add, remove, change the tuple items first we should conver the tuple into list.
Then perform operation on that list and convert it back to tuple.

'''
# conversion operations
countries = ("spain", "italy", "india", "england", "germany")
print("before update : ",countries)
temp = list(countries)
temp.append("Russia")
temp.pop(3)
temp[2] = "finland"
countries = tuple(temp)
print("after update : ",countries)

'''
However, we can concatenate two tuples without converting them.

'''
# concat operation
tup1 = (1,2,3,4,5)
tup2 = (6,7,8,9,10)
merge = tup1 + tup2
print(merge)

'''
Python has only 2 built-in tuple methods.
Method	Description	Example
count()	Returns the number of times an element appears.	t.count(2)
index()	Returns the index of the first occurrence of an element.	t.index(3)

'''
t = (1, 2, 3, 2, 4, 2)
# 1. count()
print(t.count(2))  # Output: 3
# 2. index()
print(t.index(3))  # Output: 2
#index() with range
print(t.index(3,1,4))  # Output: 2

'''
Although these are not tuple methods, they are commonly used with tuples.
Operation	Example	Result
Length	len(t)	Number of elements
Maximum	max(t)	Largest element
Minimum	min(t)	Smallest element
Sum	sum(t)	Sum of numeric elements
Sorting	sorted(t)	Returns a sorted list
Membership	2 in t	True if present
Concatenation	(1, 2) + (3, 4)	(1, 2, 3, 4)
Repetition	(1, 2) * 2	(1, 2, 1, 2)

'''
