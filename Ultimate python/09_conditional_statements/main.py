# 1) if else :
a = int(input("Enter your age : "))
print("your age is :", a)
if (a >= 18):
	print("you can drive")
else:
	print("you cannot drive")

# 2) elif
val = int(input("Enter your value : "))
if(val < 0):
	print("Number is negative")
elif(val == 0):
	print("Number is zero")
else:
	print("Number is positive")

# 3) Nested if else
num = int(input("Enter the lucky number : "))
if(num < 0):
	print("number is invalid")
elif(num > 0):
	if(num <= 10):
		print("Congratulations you are in top 10 winners")
	elif(num > 10 and num <= 20):
		print("Congratulations you made it to top 20")
	else:
		print("Better luck next time")
else:
	print("you have entered zero")


# 4) Logical if else :

# 1. and — Both conditions must be true
age = 22
has_id = False

if age >= 18 and has_id:
    print("Entry allowed")
else:
    print("Entry denied")

# 2. or — At least one condition must be true
is_weekend = False
is_holiday = False

if is_weekend or is_holiday:
    print("No work today")
else:
    print("Go to work")

# 3. not — Reverses a condition
is_raining = True

if not is_raining:
    print("Go outside")
else:
    print("Stay at home")

# 4. in — to check if exists (can be used as an alternative for methods).
name = "Python Programming"

if "Python" in name:
    print("Word found")
else:
    print("Word not found")

# 5. is - beginner-friendly use of is is checking whether a value is None.
name = None

if name is None:
    print("Name is not provided")
else:
    print("Name is provided")
