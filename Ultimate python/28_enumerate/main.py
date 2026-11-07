'''
In Python, the enumerate() function is a built-in function that adds a counter to an iterable and returns pairs of index and value.

'''

# 1. Basic enumerate function with lists
fruits = ["Apple", "Banana", "Mango"]
for index, fruit in enumerate(fruits):
    print(index, fruit)

# 2. Starting with a different index enumerate(iterable, start=0)
bikes = ["Kawasaki", "Suzuki", "Ducati"]
for index, bike in enumerate(bikes, start=1):
    print(index, bike)

# 3. Enumerate function with tuples.
eles = (1,2,3,4,5,6)
for index, ele in enumerate(eles,start=2):
    print(index, ele)

# 4. Enumerate function with sets.
s = {1,1,3,3,6,2,5,4,8}
for i, d in enumerate(s,start=1):
    print(i, d)

# 5. Enumerate with list of dictionaries.
students = [
    {"id": 1, "name": "John", "age": 20},
    {"id": 2, "name": "Alice", "age": 21},
    {"id": 3, "name": "Bob", "age": 22},
    {"id": 4, "name": "David", "age": 23},
    {"id": 5, "name": "Emma", "age": 24}
]
for i, dit in enumerate(students):
    print(i,dit)
