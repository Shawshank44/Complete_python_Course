'''
Complete Guide to Dictionaries in Python (Without Methods)
A dictionary in Python is a built-in data type that stores data in key-value pairs.
- Each key is unique.
- Values can be of any data type.
- Dictionaries are mutable (can be changed).
- Dictionaries are written using curly braces {}.
- Keys are used to access their corresponding values.

'''
# 1. Creating a Dictionary
student = {
    "name": "Rahul",
    "age": 20,
    "course": "Python",
    "marks": 95
}

print(student)

# 2. Accessing Dictionary Elements
student = {
    "name": "Rahul",
    "age": 20,
    "marks": 95
}
print(student["name"])
print(student["age"])
print(student["marks"])

# 3. Dictionary with Different Data Types
data = {
    "name": "Amit",
    "age": 21,
    "percentage": 85.5,
    "passed": True,
    "subjects": ["Python", "Java", "C"]
}
print(data)

# 4. Adding Elements to a Dictionary
student = {
    "name": "Rahul",
    "age": 20
}
student["city"] = "Bangalore"
student["marks"] = 90
print(student)

# 5. Updating Dictionary Elements
student = {
    "name": "Rahul",
    "age": 20,
    "marks": 80
}
student["marks"] = 95
student["age"] = 21
print(student)

# 6. Deleting Dictionary Elements
student = {
    "name": "Rahul",
    "age": 20,
    "marks": 90
}
del student["age"]
print(student)

# 7. Checking Whether a Key Exists
student = {
    "name": "Rahul",
    "age": 20
}
print("name" in student)
print("marks" in student)
print("city" not in student)

# 8. Finding the Length of a Dictionary
student = {
    "name": "Rahul",
    "age": 20,
    "marks": 90
}
print(len(student))

# 9. Empty Dictionary
student = {}
print(type(student))

# 10. Nested Dictionary
students = {
    "student1": {
        "name": "Rahul",
        "age": 20
    },
    "student2": {
        "name": "Amit",
        "age": 21
    }
}
print(students["student1"]["name"])
print(students["student2"]["age"])

# 11. Dictionary with Numeric Keys
numbers = {
    1: "One",
    2: "Two",
    3: "Three"
}
print(numbers[1])
print(numbers[2])

# 12. Duplicate Keys in Dictionary
student = {
    "name": "Rahul",
    "age": 20,
    "name": "Amit"
}
print(student)

# 13. Dictionary Inside a List
students = [
    {"name": "Rahul", "age": 20},
    {"name": "Amit", "age": 21},
    {"name": "Priya", "age": 19}
]
print(students[0]["name"])
print(students[1]["age"])
print(students[2]["name"])

for i in range(len(students)): # iterating through the list of dictionaries
    print(f'''name of student is {students[i]["name"]} and age of the student is {students[i]["age"]}''')

# 14. Dictionary Using Variables
name = "Rahul"
age = 20
marks = 95
student = {
    "name": name,
    "age": age,
    "marks": marks
}
print(student)

# 15. Iterating Through a Dictionary (Without Methods)
student = {
    "name": "Rahul",
    "age": 20,
    "marks": 90
}
for key in student:
    print(key, student[key])


'''
Important Dictionary Concepts
Concept	Example
Create :	d = {"a": 10}
Access :	d["a"]
Add		 :	d["b"] = 20
Update :	d["a"] = 50
Delete :	del d["a"]
Check  :	key	"a" in d
Check missing key	: "b" not in d
Length :	len(d)
Empty :	dictionary	d = {}
Loop	:	for k in d:

'''
