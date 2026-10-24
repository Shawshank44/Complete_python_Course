'''
In Python, a for loop is used to repeat a block of code for each item in a sequence, such as a list,
string, or range of numbers.

'''
# For loops :
name = "python programming"
splited = name.split()
for split in splited:
	print(split)
	for i in split: # nesting
		print(i)


# range function range(stop) : Starts from 0 and stops just before the given number.
# range function starts with zero and ends with n-1
for k in range(5):
	print(k + 1)

# range(start, stop) : Starts from the given starting number and stops just before the ending number.
for k in range(1, 21):
	print(k)

# range(start, stop, step) : The step determines how much the number increases or decreases each time.
for k in range(1, 100, 2):
	print(k)

# printing tables using loops :
val = 2
for num in range(11):
	print(val,"X",num, "=", val*num)
