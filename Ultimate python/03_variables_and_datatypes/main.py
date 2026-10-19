
# Python Variables and Data Types

# 1. Integer (int)
a = 100
print("Integer:", a)
print("Type:", type(a))

# 2. Float (float)
b = 25.5
print("\nFloat:", b)
print("Type:", type(b))

# 3. Complex (complex)
c = 3 + 4j
print("\nComplex:", c)
print("Type:", type(c))

# 4. String (str)
name = "Python"
print("\nString:", name)
print("Type:", type(name))

# 5. Boolean (bool)
is_active = True
print("\nBoolean:", is_active)
print("Type:", type(is_active))

# 6. List (list)
numbers = [10, 20, 30, 40]
print("\nList:", numbers)
print("Type:", type(numbers))

# 7. Tuple (tuple)
colors = ("red", "green", "blue")
print("\nTuple:", colors)
print("Type:", type(colors))

# 8. Range (range)
r = range(1, 6)
print("\nRange:", list(r))
print("Type:", type(r))

# 9. Dictionary (dict)
student = {"name": "Alex", "age": 20}
print("\nDictionary:", student)
print("Type:", type(student))

# 10. Set (set)
unique_numbers = {10, 20, 30, 40}
print("\nSet:", unique_numbers)
print("Type:", type(unique_numbers))

# 11. Frozen Set (frozenset)
fixed_numbers = frozenset({1, 2, 3})
print("\nFrozen Set:", fixed_numbers)
print("Type:", type(fixed_numbers))

# 12. Bytes (bytes)
byte_data = b"Hello"
print("\nBytes:", byte_data)
print("Type:", type(byte_data))

# 13. Byte Array (bytearray)
mutable_bytes = bytearray([65, 66, 67])
print("\nByte Array:", mutable_bytes)
print("Type:", type(mutable_bytes))

# 14. Memory View (memoryview)
memory_data = memoryview(b"ABC")
print("\nMemory View:", memory_data)
print("Type:", type(memory_data))

# 15. None Type (NoneType)
value = None
print("\nNone:", value)
print("Type:", type(value))

# 16. Multiple Variable Assignment
x, y, z = 10, 20, 30
print("\nMultiple Assignment:", x, y, z)

# 17. Same Value Assignment
p = q = r = 50
print("Same Value Assignment:", p, q, r)

# 18. Changing a Variable's Value
age = 18
print("\nOriginal Age:", age)
age = 21
print("Updated Age:", age)

# 19. Type Conversion
num = "123"
converted_num = int(num)
print("\nOriginal Value:", num, type(num))
print("Converted Value:", converted_num, type(converted_num))

# 20. Variable Deletion
temp = 100
del temp
print("\nVariable 'temp' has been deleted.")
# print(temp) # this is deleted (freed from memory)
