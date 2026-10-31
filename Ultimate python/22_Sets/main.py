'''
A set in Python is an unordered collection of unique elements. It does not allow duplicate values.

'''
# creating a set
a = {1,2,1,3,5,6,7,6}
print(a)

# Creating an empty set
a = set()
print(type(a))

# Accessing Elements in set:
x = {1,2,1,"carla", True, False, 5.99}
for i in x:
	print(i)

'''
in the above example True is not appearing separately because in Python sets, True is considered equal to 1.

'''

# Set operations :
# 1) Adding elements using assignment :
a = {10, 20, 30}
a = {*a, 40}
print(a)

# 2) Removing elements without methods :
a = {10, 20, 30, 40}
a = {x for x in a if x != 20}
print(a)

# 3) Set Union - Combines all elements from two sets :
a = {1, 2, 3}
b = {3, 4, 5}
print(a | b)

# 4) Set Intersection - Returns common elements :
a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)

# 5) Set Difference - Returns elements present in the first set but not in the second :
a = {1, 2, 3}
b = {2, 3, 4}
print(a - b)

# 6) Symmetric Difference - Returns elements that are not common to both sets :
a = {1, 2, 3}
b = {2, 3, 4}
print(a ^ b)

# 7) Checking membership :
a = {10, 20, 30}
print(20 in a)
print(20 not in a)

# 8) Finding set length :
a = {10, 20, 30, 40}
print(len(a))

# 9) Checking subset :
a = {1, 2}
b = {1, 2, 3, 4}
print(a <= b)

# 10) Checking superset :
a = {1, 2, 3, 4}
b = {1, 2}
print(a >= b)

# 11) Removing duplicate elements from a list :
a = [10, 20, 20, 30, 30, 40]
b = {*a}
print(b)

# 12) Set comprehension :
a = {x for x in range(1, 11) if x % 2 == 0}
print(a)


'''
Important set operators without methods
Operator	Meaning
\|	Union
&	Intersection
-	Difference
^	Symmetric difference
<=	Subset
>=	Superset
==	Equal sets
!=	Unequal sets
in	Membership
not in	Non-membership

Note: The examples above avoid set methods such as add(), remove(), discard(), union() and intersection().
They use operators, assignment and built-in functions instead.

'''
