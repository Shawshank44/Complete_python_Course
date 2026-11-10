'''
In Python, if __name__ == "__main__": is used to check whether a Python file is being run directly or imported into another Python file.

Let's break it down:
- __name__ is a special built-in Python variable.
- "__main__" is a special value assigned to __name__ when a Python file is executed directly.
- The if condition checks whether the file is running directly.

'''

import calcu

print("Main function started")
print(__name__)

calcu.add(10,5)
calcu.sub(2,1)
calcu.mul(10,5)
