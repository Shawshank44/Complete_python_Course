'''
In Python, a while loop repeats a block of code as long as a given condition is True.

'''
# While Loop :
i = 0
while (i<=5):
	print(i)
	i = i + 1

# Decrementing while loop :
print("While loop decrementing")
count = 5
while(count > 0) :
	print(count)
	count = count - 1
else: # can pass else condition
	print("Inside else condition")


# Example for understanding for loop :
password = ""
while password != "python123":
    password = input("Enter password: ")
print("Access granted!")
