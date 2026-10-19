
# Complete Python Operators in One Program

a = 10
b = 3

# 1. Arithmetic Operators
print("1. ARITHMETIC OPERATORS")
print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Modulus:", a % b)
print("Exponentiation:", a ** b)

# 2. Comparison Operators
print("\n2. COMPARISON OPERATORS")
print("Equal:", a == b)
print("Not Equal:", a != b)
print("Greater Than:", a > b)
print("Less Than:", a < b)
print("Greater Than or Equal:", a >= b)
print("Less Than or Equal:", a <= b)

# 3. Assignment Operators
print("\n3. ASSIGNMENT OPERATORS")
x = 10
print("Assignment:", x)

x += 5
print("Add and Assign:", x)

x -= 2
print("Subtract and Assign:", x)

x *= 2
print("Multiply and Assign:", x)

x /= 2
print("Divide and Assign:", x)

x = 10
x //= 3
print("Floor Divide and Assign:", x)

x = 10
x %= 3
print("Modulus and Assign:", x)

x = 2
x **= 3
print("Exponent and Assign:", x)

x = 10
x &= 3
print("Bitwise AND and Assign:", x)

x = 10
x |= 3
print("Bitwise OR and Assign:", x)

x = 10
x ^= 3
print("Bitwise XOR and Assign:", x)

x = 10
x <<= 1
print("Left Shift and Assign:", x)

x = 10
x >>= 1
print("Right Shift and Assign:", x)

# 4. Logical Operators
print("\n4. LOGICAL OPERATORS")
p = True
q = False
print("AND:", p and q)
print("OR:", p or q)
print("NOT:", not p)

# 5. Bitwise Operators
print("\n5. BITWISE OPERATORS")
a = 10
b = 3
print("Bitwise AND:", a & b)
print("Bitwise OR:", a | b)
print("Bitwise XOR:", a ^ b)
print("Bitwise NOT:", ~a)
print("Left Shift:", a << 1)
print("Right Shift:", a >> 1)

# 6. Membership Operators
print("\n6. MEMBERSHIP OPERATORS")
numbers = [10, 20, 30, 40]
print("10 in numbers:", 10 in numbers)
print("50 not in numbers:", 50 not in numbers)

# 7. Identity Operators
print("\n7. IDENTITY OPERATORS")
list1 = [1, 2, 3]
list2 = list1
list3 = [1, 2, 3]

print("list1 is list2:", list1 is list2)
print("list1 is list3:", list1 is list3)
print("list1 is not list3:", list1 is not list3)

# 8. Conditional Expression (Ternary Operator)
print("\n8. CONDITIONAL EXPRESSION")
age = 20
result = "Eligible" if age >= 18 else "Not Eligible"
print("Voting Status:", result)

# 9. Walrus Operator (:=)
print("\n9. WALRUS OPERATOR")
if (n := len(numbers)) > 3:
    print("List length:", n)

# 10. Matrix Multiplication Operator (@)
print("\n10. MATRIX MULTIPLICATION OPERATOR")
# Requires NumPy for matrix multiplication
# import numpy as np
# A = np.array([[1, 2], [3, 4]])
# B = np.array([[5, 6], [7, 8]])
# print(A @ B)

# 11. Operator Precedence Example
print("\n11. OPERATOR PRECEDENCE")
result = 2 + 3 * 4
print("2 + 3 * 4 =", result)

result = (2 + 3) * 4
print("(2 + 3) * 4 =", result)
