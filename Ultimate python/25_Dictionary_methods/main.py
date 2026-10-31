# Dictionary Methods in Python
# 1. clear() - Removes all elements from the dictionary.
student = {
    "name": "John",
    "age": 25,
    "course": "Python"
}
student.clear()
print(student)

# 2. copy() - Creates a shallow copy of the dictionary.
student = {
    "name": "John",
    "age": 25
}
new_student = student.copy()
print(new_student)
# You can modify the copied dictionary without changing the original when modifying top-level values.
new_student["age"] = 30
print(student)
print(new_student)
# Important: copy() creates a shallow copy, not a deep copy. Nested mutable objects are still shared.

# 3. fromkeys() - Creates a new dictionary using the given keys and assigns the same value to every key.
keys = ["name", "age", "course"]
student = dict.fromkeys(keys, "Unknown")
print(student)
# Without providing a value:
student = dict.fromkeys(keys)
print(student)


# 4. get() - Returns the value associated with a specified key.
student = {
    "name": "John",
    "age": 25
}
print(student.get("name"))
print(student.get("age"))
# You can provide a default value:
print(student.get("marks", 0))
# Important: get() does not produce a KeyError when the key is missing.


# 5. items() - Returns all dictionary key-value pairs as a view of dictionary items.
student = {
    "name": "John",
    "age": 25,
    "course": "Python"
}
print(student.items())
# Using a loop:
for key, value in student.items():
    print(key, value)

# 6. keys() - Returns all keys in the dictionary.
student = {
    "name": "John",
    "age": 25,
    "course": "Python"
}
print(student.keys())
# Using a loop:
for key in student.keys():
    print(key)


# 7. pop() - Removes the specified key and returns its corresponding value.
student = {
    "name": "John",
    "age": 25,
    "course": "Python"
}
result = student.pop("age")
print(result)
print(student)


# 8. popitem() - Removes and returns the last inserted key-value pair.
student = {
    "name": "John",
    "age": 25,
    "course": "Python"
}
result = student.popitem()
print(result)
print(student)


# 9. setdefault() - Returns the value of a specified key If the key doesn't exist, it inserts the key with the specified default value..
student = {
    "age": 25,
    "city" : "bengaluru",
    "State" : "karnataka"
}
result = student.setdefault("name", "Guest")
print(result)
student["name"] = "ravi" # overwriting the default value
print(student)


# 10. update() - Updates an existing dictionary with new key-value pairs.
student = {
    "name": "John",
    "age": 25
}
student.update({"age": 30}) #Updating an existing key.
student.update({"city" : "Pune", "state" : "Maharashtra"}) #Adding new keys.
student.update(bloodGroup="o+", rollnumber=2235) # update using keyword arguments
print(student)


# 11. values() - Returns all values in the dictionary.
student = {
    "name": "John",
    "age": 25,
    "course": "Python"
}
print(student.values())
# Using a loop:
for value in student.values():
    print(value)


'''
All Dictionary Methods
clear()	Removes all items
copy()	Creates shallow copy
fromkeys()	Creates dictionary from keys
get()	Retrieves a value
items()	Returns key-value pairs
keys()	Returns all keys
pop()	Removes specified key
popitem()	Removes last inserted item
setdefault()	Gets value or inserts key
update()	Adds or updates key-value pairs
values()	Returns all values
'''
