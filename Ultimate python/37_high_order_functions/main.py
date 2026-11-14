'''
Complete Guide to Python Higher-Order Functions: map(), filter(), reduce() and sorted()
These four functions are important in Python because they allow you to process collections such as lists, tuples, strings, and other iterables using functions.

'''

from functools import reduce

# 1. map() – Transform elements - The map() function applies a given function to every element of an iterable.
l = [1,2,3,4,5,6,7,8,9,10]
multiply = map(lambda x : x * x, l)
print(multiply) # return a memory object
print(list(multiply))

# Mapping multiple iterables
# map() accepts multiple iterables if the supplied function accepts the corresponding number of arguments.
a = [1, 2, 3]
b = [10, 20, 30]
result = map(lambda x, y: x + y, a, b)
print(list(result))

# Using a built-in function and different datatypes :
numbers = [1, 2, 3, 4, 5]
result_list = list(map(str, numbers))
result_tuple = tuple(map(float, numbers))
result_set = set(map(int, numbers))
print(result_list)
print(result_tuple)
print(result_set)

# Using a custom function
def square(n):
    return n ** 2
numbers = [1, 2, 3, 4, 5]
result = map(square, numbers)
print(list(result))

# Mapping strings :
names = ["john", "alex", "shashank"]
result = map(str.upper, names)
print(list(result))


# 2. filter() – Filter elements - The filter() function selects elements from an iterable based on a condition.
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even = list(filter(lambda x: x % 2 == 0, numbers))
odd = list(filter(lambda x: x % 2 != 0, numbers))
print("Even :", even)
print("Odd : ", odd)

# Using a custom function :
def is_positive(n):
    return n > 0
nums = [-10, -5, 0, 5, 10, 15]
res = list(filter(is_positive, nums))
print(res)

# Filter strings based on length
names = ["John", "Alex", "Christopher", "Sam", "Alexander"]
result = filter(lambda name: len(name) > 4, names)
print(list(result))

# Filter using multiple conditions
n = [1,2,3,4,5,30,60,90,120,399]
calcu = list(filter(
    lambda x : x > 20 and x % 2 == 0,
    n
))
print(calcu)

# Filter non-empty strings
names = ["John", "", "Alex", "", "Sam"]
result = list(filter(None, names))
print(result)


# 3. reduce() – Reduce elements into a single value. Combines iterable elements into a single accumulated result.
# It is available through the functools module.
ele = [1,2,3,4,5,6,7,10]
result_add = reduce(lambda x, y : x + y, ele)
result_mul = reduce(lambda x, y : x * y, ele)
result_max = reduce(lambda x, y: x if x > y else y, ele)
result_min = reduce(lambda x, y: x if x < y else y, ele)
result_initializer = reduce(lambda x, y: x + y, ele, 100) # Optional starting value.
print(result_add)
print(result_mul)
print(result_max)
print(result_min)
print(result_initializer)

# Concatenate strings
words = ["Python", " ", "is", " ", "awesome"]
result = reduce(lambda x, y: x + y, words)
print(result)


# 4. sorted(iterable, key=None, reverse=False) – Sort elements function returns a new sorted list from an iterable.
numbers = [50, 10, 40, 20, 30]
result = sorted(numbers)
res_reverse = sorted(numbers, reverse=True) # Sort numbers in descending order
print(result)
print(res_reverse)

# Sort strings alphabetically
names = ["Shashank", "John", "Alex", "David"]
result = sorted(names)
print(result)

# Sort strings by length - This is where the key argument becomes useful.
names = ["Christopher", "Sam", "Alexander", "John"]
result = sorted(names, key=len)
print(result)

# Sort using lambda
numbers = [15, 3, 25, 8, 12]
result = sorted(numbers, key=lambda x: x % 10) # The sorting is based on each number's remainder when divided by 10.
print(result)

# Sort dictionaries by a particular value
students = [
    {"name": "John", "marks": 80},
    {"name": "Alex", "marks": 95},
    {"name": "Sam", "marks": 70}
]
result = sorted(students, key=lambda x: x["marks"])
result_reverse = sorted(students, key=lambda x: x["marks"], reverse=True) # Sort dictionaries in descending order
mul_condition = sorted(students,key=lambda x: (-x["marks"], x["name"])) # Sort by multiple conditions
print(result)
print(result_reverse)
print(mul_condition)


# 5. Combining higher-order functions
salaries = [25000, 35000, 45000, 20000, 60000, 50000]
# Step 1: Filter salaries
filtered = filter(lambda x: x > 30000, salaries)
# Step 2: Increase salary by 10%
increased = map(lambda x: x * 1.10, filtered)
# Step 3: Sort descending
sorted_salaries = sorted(increased, reverse=True)
# Step 4: Calculate total
total = reduce(lambda x, y: x + y, sorted_salaries, 0)
print("Sorted salaries:", sorted_salaries)
print("Total:", total)


'''
Important concepts to understand
- Higher-order functions: Functions that accept other functions as arguments or return functions.
- Lambda: Anonymous function used for short operations.
- Iterable: An object that can be iterated over, such as lists, tuples, and strings.
- Iterator: An object that produces elements one at a time.
- Lazy evaluation: Processing values when they are requested rather than immediately.
- Callback function: A function passed as an argument to another function.

recommendation: Since you're learning Python fundamentals,
focus on understanding how functions are passed as arguments before relying heavily on lambda expressions.
You should be able to write the same logic using a normal def function first. Then learn to express it using lambda, map(), and filter().
This builds actual programming logic instead of just memorizing syntax.

'''
