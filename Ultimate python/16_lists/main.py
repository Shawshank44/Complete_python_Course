'''
In Python, a list is a collection used to store multiple items in a single variable.
Lists are ordered, mutable (changeable), and allow duplicate values and different data types.

'''

# Empty list
a = []

# List of integers
numbers = [10, 20, 30, 40]

# List of strings
names = ["Ram", "Sam", "Ravi"]

# Mixed data types
items = [10, "Hello", 3.5, True]

print(numbers)
print(names)
print(items)
numbers[0] = 100 # updating a list element.
numbers[1:3] = [200, 300] # updating a range list element.
print(numbers)

# Accessing list elements with indexing
a = [10, 20, 30, 40, 50]
print(a[0])   # 10
print(a[2])   # 30
print(a[-1])  # 50 (last element)
print(a[-2])  # 40
print(a[len(a)-3]) # converting negative index to positive.


# Concatenation — +
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)  # [1, 2, 3, 4, 5, 6]

# Repetition — *
nums = [1, 2, 3]
print(nums * 2)  # [1, 2, 3, 1, 2, 3]
print(nums * 3)  # [1, 2, 3] repeated three times
print(nums * 0)  # []
print(nums * -1) # []


# validating list elements using "in" keyword
if 70 in a:
	print("yes")
else:
	print("no")

# Accessing elements using list[start:end:jumpindex]
names = ["ram", "sham", "sam", "kumar", "umar", 1, 2, 3, 4, 5]
print(names[1:-1]) # print(names[1:len(names)-1])
print(names[1:8])
print(names[1:8:3]) # jump index.

'''
				JUMP INDEX VISUAL
  1                        2           3
['sham', 'sam', 'kumar', 'umar', 1, 2, 3]
		|                      |           |
		|______					_______|		       |
					|					|	 	 ______________|
				['sham', 'umar', 3]
'''


# List Comprehension :
lst = [i for i in range(4)]
print(lst)

# List Comprehension with condition :
lst1 = [i for i in range(20) if i % 2 == 0]
print(lst1)

infos = ["milo","sarah","bruno","anastasia","rosa"]
infosWith_0 = [info for info in infos if "o" in info]
infosWith_char = [info for info in infos if (len(info) > 4)]
print(infosWith_0)
print(infosWith_char)



# Multi dementional list :
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(matrix[0])     # [1, 2, 3]
print(matrix[1][2])  # 6
for row in matrix:
    for value in row:
        print(value, end=" ")
    print()


# Lists inside functions :
def get_list(items):
    return items

lis = [1,2,3,4,5,6,7,8,9,10]
num = get_list(lis)

print("List elements from function:", num)



# Deletion of elements using "del" keyword
ele = [10, 20, 30, 40, 50]

del ele[0]
print(ele)  # [20, 30, 40, 50]

del ele[1:3]
print(ele)  # [20, 50]

del ele[-1]
print(ele)  # [20]

del ele[:]
print(numbers)  # []
