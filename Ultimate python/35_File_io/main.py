'''
File I/O (File Input/Output) in Python means reading data from files and writing data into files. Python provides built-in functions to create, open, read, write, append, and close files.
1. Types of Files
Python mainly supports two types of files:
1. Text Files: Store data in readable text format.
   - .txt
   - .csv
   - .py
   - .json
2. Binary Files: Store data in binary format.
   - .jpg
   - .png
   - .mp3
   - .pdf
   - .exe

File Opening Modes
Mode - Description
r - Read a file
w - Write to a file (overwrites existing content)
a - Append content to a file
x - Create a new file; error if it exists
r+ - Read and write
w+ - Write and read (overwrites)
a+ - Append and read
rb - Read binary file
wb - Write binary file
ab - Append binary data


'''

import os

# Opening a File - Python uses the open() function to open a file - file = open("filename.txt", "mode").
f = open("myfile.txt") # by default open function will be in read mode. if we do not mention 'r'
text = f.read()
print(text)
f.close()

# file operations using modes :
# 1. Read :
file = open("myfile.txt",'r')
textf = file.read()
print(textf)
file.close()

# 2. Write :
file = open("demo.txt",'w')
file.write("Welcome to python file operations \n")
file.write("Learning File Handling")
file.close()

# 3. append :
file = open("demo.txt",'a')
# file.write("python is very easy to learn \n")
file.write("python is dynamically typed language. \n")
file.close()

# 4. creating a file with error handling:
try:
	file = open("mytest.txt",'x')
	file.write("this file handling with error")
	file.close()
except FileExistsError as e:
	print(e)

# read(), readline(), and readlines() method for file operations :
file = open("myread.txt",'r')
# data = file.read()
# data = file.read(5) # Read only the first five characters:
# data = file.readline() # Reads one line at a time.
data = file.readlines() # Reads all lines and returns them as a list.
print(data)
file.close()

# Writelines method for file operations :
sentences = [
    "Although the morning started with heavy rainfall and dark clouds covering the entire sky, the students decided to continue their journey toward the university because they had an important examination scheduled for that afternoon. \n",
    "Technology has significantly transformed the way people communicate, allowing individuals from different countries and cultures to exchange ideas, collaborate on projects, and share valuable information within seconds. \n",
    "The young entrepreneur spent several months researching market trends, analyzing customer behavior, and developing an innovative business strategy before finally launching her first successful technology startup. \n",
    "While exploring the beautiful countryside during their summer vacation, the travelers discovered a small village surrounded by mountains, green forests, and peaceful rivers that created an unforgettable experience. \n",
    "Artificial intelligence is rapidly changing modern industries by automating repetitive tasks, improving decision-making processes, and helping organizations develop more efficient solutions to complex real-world problems. \n",
    "Despite facing numerous challenges and unexpected failures throughout the competition, the dedicated engineering team continued improving their prototype until they successfully developed a solution that exceeded everyone's expectations. \n",
    "Reading books regularly can improve vocabulary, strengthen critical thinking abilities, expand imagination, and provide readers with valuable perspectives about different cultures, historical events, and human experiences. \n"
]
file = open("mywrite.txt",'w')
lines = file.writelines(sentences)
file.close()


# Using the with Statement - The with statement automatically closes a file after its block finishes.
# It is the recommended way to handle files in Python.
with open("mywrite.txt",'r') as file:
	data = file.readlines()
	print(data)
# No need to call close() manually.


# File Pointer Methods - Python provides methods to manage the file pointer.
# 1. tell() - Returns the current position of the file pointer.
with open("mywrite.txt", "r") as file:
    print(file.tell())
    file.read(5)
    print(file.tell())

# 2. seek() - Moves the file pointer to a specified position.
with open("mywrite.txt", "r") as file:
    file.seek(5)
    print(file.read())

# 3. truncate()
with open("demo.txt",'w') as f :
	f.write("Hello World")
	f.truncate(5)


# Renaming a File - Use the os.rename() function.
os.rename("demo.txt", "newdemo.txt")

# Deleting a File Use os.remove() to delete a file.
os.remove("newdemo.txt")

# Check whether a file exists:
if os.path.exists("demo.txt"):
    print("File exists")
else:
    print("File does not exist")


# Reading lines, words, characters :
with open("mywrite.txt", "r") as file:
    data = file.read()

lines = data.splitlines()
words = data.split()
characters = len(data)

print("Lines:", len(lines))
print("Words:", len(words))
print("Characters:", characters)


'''
Important File I/O Functions Summary
Function - Purpose
open() - Opens a file
read() - Reads file content
readline() - Reads one line
readlines() - Reads all lines into a list
write() - Writes a string
writelines() - Writes multiple strings
close() - Closes a file
seek() - Moves file pointer
tell() - Returns file pointer position
flush() - Flushes buffered data

Recommendation: Learn the file modes first, then practise read(), write(), append(), seek() and tell().
Finally, build a student management system using file handling. These concepts form the foundation of Python File I/O.

'''
