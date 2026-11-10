'''
The Python os module provides functions to interact with the operating system.
It helps you work with files, folders, directories, environment variables, and system information.

'''

import os
import subprocess


# 1. Getting current directory
print(os.getcwd())

# 2. Working with directories
if (not os.path.exists("test")): # check the directory if exists ?
	os.mkdir("test") # Creates a single directory.

os.chdir(r"C:\Users\Shashank.BR\OneDrive\Desktop\Python\Ultimate python\32_os_module\test") # Changes the current working directory.
# "r" keyword is known as raw string It tells Python to treat backslashes (\) as literal characters instead of interpreting them as escape sequences.

if (not os.path.exists("parent/child/grandchild")):
	os.makedirs("parent/child/grandchild") # Creates nested directories.

print(os.listdir()) # Lists files and folders, List files in a particular directory os.listdir("C:/Users"):.


with os.scandir(".") as entries: # Efficiently scans (loops/iterates) directory entries.
	for entry in entries:
		print(entry.name)

os.rmdir("test2") # Removes an empty directory.

os.remove("test.txt") # Deletes a file.

os.removedirs("parent/child/grandchild") # Removes empty nested directories.

os.rename("test","Test") # Renames a file or directory.
os.replace("Test","TEST") # Replaces a destination directory or renames a directory.

info = os.stat("TEST")
print(info.st_size)   # File size in bytes
print(info.st_mtime)  # Last modification time
print(info.st_ctime)  # Metadata change time on Unix


# 4. Checking directories - The os.path submodule provides useful path functions.
print(os.path.exists("test.txt"))
print(os.path.isfile("test.txt"))
print(os.path.isdir("myfolder"))
print(os.path.isabs("C:/Users"))
print(os.path.getsize("TEST"))
print(os.path.getmtime("TEST"))

'''
Function - Purpose
exists() - Checks whether path exists
isfile() - Checks whether it is a file
isdir() - Checks whether it is a directory
isabs() - Checks whether path is absolute
getsize() - Gets file size
getmtime() - Gets modification time
getatime() - Gets last access time
getctime() - Gets creation time on Windows; metadata change time on Unix

'''

# 5. Joining and splitting paths os.path.join() – Joins path components correctly.
path = os.path.join("C:", "Users", "Admin", "file.txt") # Joins path components correctly.
print(path)

print(os.path.basename("C:/Users/Admin/file.txt")) # Returns filename.

print(os.path.dirname("C:/Users/Admin/file.txt")) # Returns directory name.

print(os.path.split("C:/Users/Admin/file.txt")) # Splits path into directory and filename.

print(os.path.splitext("document.pdf")) # Splits filename and extension.

print(os.path.abspath("test.txt")) # Returns absolute path.

print(os.path.normpath("folder//subfolder/../file.txt")) # Normalizes a path.


# 6. Environment variables
print(os.environ) # Accesses environment variables.

print(os.environ.get("APPDATA")) # Get a variable:

os.environ["MY_NAME"] = "Python" # Set a variable for the current process and its children:
print(os.environ["MY_NAME"])

os.environ.pop("MY_NAME", None) # Delete an environment variable

print(os.getenv("USERNAME")) # Gets an environment variable.

# 7. System information
print(os.name) # Returns the operating system family.

print(os.cpu_count()) # Returns the number of logical CPUs.

print(os.getlogin()) # Returns the login name.

print(os.getpid()) # Returns current process ID.

print(os.getppid()) # Returns parent process ID (where supported).


# 8. Running system commands
os.system("echo Hello World") # (deprecated) Executes a command through the system shell.

# Alternative for os.system is :
subprocess.run("echo Hello World", shell=True)

# 9. Walking through directories
for root, dirs, files in os.walk("."): # Traverses a directory tree.
    print("Current folder:", root)
    print("Directories:", dirs)
    print("Files:", files)

for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".py"):
            print(os.path.join(root, file))


# 10. File permissions
print(os.access("test.txt", os.F_OK)) # File exists
print(os.access("test.txt", os.R_OK)) # Read permission
print(os.access("test.txt", os.W_OK)) # Write permission
print(os.access("test.txt", os.X_OK)) # Execute permission


'''
Other useful functions
Function - Description
os.sep - Path separator
os.pathsep - Separator used in PATH variables
os.linesep - Platform-specific line separator
os.curdir - Current directory symbol (.)
os.pardir - Parent directory symbol (..)
os.defpath - Default executable search path
os.urandom(n) - Generates n random bytes
os.path.commonpath() - Finds common path
os.path.commonprefix() - Finds common string prefix
os.path.expanduser() - Expands ~ to home directory
os.path.expandvars() - Expands environment variables
os.path.samefile() - Checks whether paths refer to same file
os.path.relpath() - Gets relative path
os.sync() - Flushes filesystem buffers (where supported)


Important os module cheat sheet
Category - Functions
Directory - getcwd, chdir, listdir, scandir, mkdir, makedirs
Remove - remove, rmdir, removedirs
Rename - rename, replace
File - information	stat, access
Path - join, split, exists, basename, dirname
Environment - environ, getenv, putenv
System - name, cpu_count, getpid, getlogin
Process - system, getppid
Directory traversal - walk, fwalk
Permissions - chmod, access, chown
Random bytes - urandom

Note: Some functions are platform-dependent. For complete documentation, visit the official Python reference:
https://docs.python.org/3/library/os.html?utm_source=chatgpt.com

Recommendation: Learn os.getcwd(), os.listdir(), os.mkdir(), os.makedirs(), os.remove(), os.walk() and os.path.join() first.
These are especially useful for automation, file management, and Python scripting.

'''
