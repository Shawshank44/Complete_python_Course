# In Python, both is and == are used for comparison, but they check different things.

a = 4
b = "4"
print(a is b) # compares the identity
print(a == b) # compares the value

# Both are same comparision operators.

# 1. == — Checks value equality - It checks whether two objects have the same value.
a = [1, 2, 3]
b = [1, 2, 3]
print(a == b)  # True
# Why? Both lists contain the same elements.

# 2. is — Checks object identity - It checks whether two variables refer to the exact same object in memory.
a = [1, 2, 3]
b = [1, 2, 3]
print(a is b)  # False
# Why? They are two separate list objects, even though their values are identical.

'''
3. Visual comparison

(Using ==)
a [1, 2, 3] = b[1, 2, 3]

True
Same values.

(Using is)
a[1, 2, 3] Object 1 ≠ b [1, 2, 3] Object 2

False
Different objects in memory.

'''
# 4. When can both return True?
a = [1, 2, 3]
b = a
print(a == b)  # True
print(a is b)  # True

# 5. Important interview question why should you use is None instead of == None?
x = None
if x is None:
    print("No value")

# Best practice: Use is None or is not None when checking for None.

'''
6. Quick comparison
Feature	== - is
Checks - Values - Object identity
Compares contents - Yes - No
Checks same object - No - Yes
Common use - Value comparison - None checking

Remember
- == → Are they equal?
- is → Are they the same object?

'''
