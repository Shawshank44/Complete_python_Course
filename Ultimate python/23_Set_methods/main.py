# Set Methods :
# 1. add() - Adds a single element to a set.
s = {1, 2, 3}
s.add(4)
print(s)

# 2. update() - Adds multiple elements to a set.
s = {1, 2, 3}
s.update([4, 5, 6])
print(s)

# 3. remove() - Removes a specified element. Raises KeyError if the element doesn't exist.
s = {10, 20, 30}
s.remove(20)
print(s)

# 4. discard() - Removes an element without raising an error if it doesn't exist.
s = {10, 20, 30}
s.discard(50)
print(s)

# 5. pop() - Removes and returns an arbitrary element.
s = {10, 20, 30}
x = s.pop()
print(x)
print(s)

# 6. clear() - Removes all elements from the set.
s = {1, 2, 3}
s.clear()
print(s)

# 7. copy() - Creates a copy of the set.
s1 = {1, 2, 3}
s2 = s1.copy()
print(s2)

# 8. union() - Combines two sets without duplicates.
a = {1, 2, 3}
b = {3, 4, 5}
print(a.union(b))

# 9. intersection() - Returns common elements.
a = {1, 2, 3}
b = {2, 3, 4}
print(a.intersection(b))

# 10. difference() - Returns elements present in the first set but not in the second.
a = {1, 2, 3}
b = {2, 3, 4}
print(a.difference(b))

# 11. symmetric_difference() - Returns elements that are not common to both sets.
a = {1, 2, 3}
b = {2, 3, 4}
print(a.symmetric_difference(b))

# 12. intersection_update() - Keeps only common elements and updates the original set.
a = {1, 2, 3}
b = {2, 3, 4}
a.intersection_update(b)
print(a)

# 13. difference_update() - Removes common elements from the original set.
a = {1, 2, 3}
b = {2, 3, 4}
a.difference_update(b)
print(a)

# 14. symmetric_difference_update() - Keeps only non-common elements.
a = {1, 2, 3}
b = {2, 3, 4}
a.symmetric_difference_update(b)
print(a)

# 15. issubset() - Checks whether all elements of one set exist in another set.
a = {1, 2}
b = {1, 2, 3, 4}
print(a.issubset(b))

# 16. issuperset() - Checks whether a set contains all elements of another set.
a = {1, 2, 3, 4}
b = {1, 2}
print(a.issuperset(b))

# 17. isdisjoint() - Checks whether two sets have no common elements.
a = {1, 2, 3}
b = {4, 5, 6}
print(a.isdisjoint(b))


'''
Complete Set Methods in Python
Method	Description
add()	Adds an element to a set
update()	Adds multiple elements
remove()	Removes an element; gives an error if absent
discard()	Removes an element; no error if absent
pop()	Removes and returns an arbitrary element
clear()	Removes all elements
copy()	Returns a shallow copy
union()	Returns all unique elements from sets
intersection()	Returns common elements
difference()	Returns elements present in the first set only
symmetric_difference()	Returns elements present in either set but not both
intersection_update()	Updates the set with common elements
difference_update()	Removes elements found in another set
symmetric_difference_update()	Updates the set with non-common elements
issubset()	Checks whether a set is a subset
issuperset()	Checks whether a set is a superset
isdisjoint()	Checks whether two sets have no common elements

Important Points About Sets
1. Sets do not allow duplicate elements.
2. Sets are unordered.
3. Sets are mutable.
4. Sets do not support indexing or slicing.
5. Set elements must be immutable (hashable).
6. Sets can contain different data types.
7. An empty set is created using set(), not {}.
8. A frozenset is an immutable version of a set.

Remember the difference between remove() and discard(), and between difference() and symmetric_difference().
These are commonly tested Python set concepts.

'''
