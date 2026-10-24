'''
In Python, break and continue are used to control how a loop runs. The main difference is:
- break → stops the loop completely.
- continue → skips the current iteration and moves to the next one.

'''
# break :
for i in range (12):
	if(i == 10):
		break
	print("5 X", i+1, "=", 5 * (i+1))
print("Loop exited")

# Continue :
for i in range (12):
	if(i == 10):
		print("skipped the iteration")
		continue
	print("5 X", i+1, "=", 5 * (i+1))
print("Loop exited")


# Emulating the do while in python using break and continue :
# Break :
password = ""
while True:
	password = input("Enter the password : ")
	if (password == "python123"):
		print("Access granted")
		break
	else:
		print("access denied")
		continue
