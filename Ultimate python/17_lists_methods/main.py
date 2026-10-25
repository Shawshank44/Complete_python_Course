# 1. append()
numbers = [1, 2, 3]
numbers.append(4)
print("1. append()", numbers)
# [1, 2, 3, 4]

# 2. extend()
numbers = [1, 2]
numbers.extend([3, 4])
print("2. extend()",numbers)
# [1, 2, 3, 4]

# 3. insert()
numbers = [1, 3]
numbers.insert(1, 2)
print("3. insert()",numbers)
# [1, 2, 3]

# 4. remove()
numbers = [1, 2, 2, 3]
numbers.remove(2)
print("4. remove()",numbers)
# [1, 2, 3]

# 5. pop()
numbers = [10, 20, 30]
print("5. pop()",numbers.pop()) # removes element from end of the list.
# 30
print("5. pop() with index",numbers.pop(0))
# 10
print("5. pop() popped list",numbers)
# [20]

# 6. clear()
numbers = [1, 2, 3]
numbers.clear()
print("6. clear()",numbers)
# []

# 7. index()
numbers = [10, 20, 30, 20]
print("7. index()",numbers.index(20))
# 1

# 8. count()
numbers = [1, 2, 2, 3, 2]
print("8. count()",numbers.count(2))
# 3

# 9. sort()
numbers = [4, 1, 3, 2]
numbers.sort()
print("9. sort()",numbers)
# [1, 2, 3, 4]

numbers.sort(reverse=True)
print("9. sort() reverse ",numbers)
# [4, 3, 2, 1]

# 10. reverse()
numbers = [1, 2, 3]
numbers.reverse()
print("10. reverse()",numbers)
# [3, 2, 1]

# 11. copy()
original = [1, 2, 3]
new_list = original.copy()
new_list.append(4)
print("11. copy()",original)  # [1, 2, 3]
print("11. copy() new list",new_list)  # [1, 2, 3, 4]


'''
Python also has built-in functions that work with lists, but these are not list methods.
Function	Purpose	Example
len()	Returns the number of items	len([1, 2, 3]) → 3
max()	Returns the largest item	max([1, 5, 3]) → 5
min()	Returns the smallest item	min([1, 5, 3]) → 1
sum()	Adds numeric items	sum([1, 2, 3]) → 6
sorted()	Returns a new sorted list	sorted([3, 1, 2]) → [1, 2, 3]
any()	Checks whether any item is truthy	any([0, 1]) → True
all()	Checks whether all items are truthy	all([1, 2]) → True
list()	Creates a list	list("abc") → ['a', 'b', 'c']

Remember: There are exactly 11 public list methods in Python's standard built-in list type.

'''
