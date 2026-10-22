num = input("Enter the number like (num + num) : ")
splitinput = num.split()
a = int(splitinput[0])
b = int(splitinput[2])
opr = splitinput[1]

match opr:
	case _ if (a <= 0) or (b <= 0):
		print("only positive numbers are allowed")
	case '+':
		print("addition : ", a+b)
	case '-':
		print("subtraction : ",a-b)
	case ('*' | 'X'): # "or" statement for pattern matching.
		print("multiply : ", a*b)
	case ('/' | '%'):
		print("divide : ", a/b)
	case _ : # default case.
		print("Enter the number in valid format please.")


'''
Note : “In Python match-case, "or" becomes "|" only when matching alternative patterns,
while "and", "not", "or" remain the same in guard conditions (if).”

'''
