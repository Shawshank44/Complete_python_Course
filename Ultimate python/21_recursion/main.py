'''
Recursion is a programming technique in which a function calls itself to solve a problem by breaking it into smaller subproblems.

'''

# Factorial(7) = 7*6*5*4*3*2*1
# Factorial(6) = 6*5*4*3*2*1
# Factorial(5) = 5*4*3*2*1
# Factorial(4) = 4*3*2*1
# Factorial(3) = *3*2*1
# Factorial(0) = 1 - by default

# factorial example with recursion
def factorial(n):
	if(n==0 or n==1): # Base case
		return 1
	else:
		return n * factorial(n-1) # Recursive call

print(factorial(3))

# Sum of first N natural numbers example
def sum_n(n):
    if n == 0:
        return 0
    return n + sum_n(n - 1)

print(sum_n(5))

# Fibonacci series
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

for i in range(7):
    print(fibonacci(i), end=" ")

# Reverse a string
def reverse_string(s):
    if len(s) <= 1:
        return s
    return reverse_string(s[1:]) + s[0]

print(reverse_string("python"))

# Calculate the power of a number
def power(a, n):
    if n == 0:
        return 1
    return a * power(a, n - 1)

print(power(2, 4))


# Find the sum of digits
def digit_sum(n):
    if n == 0:
        return 0
    return n % 10 + digit_sum(n // 10)

print(digit_sum(1234))


# Print numbers from 1 to N
def print_numbers(n):
    if n == 0:
        return
    print_numbers(n - 1)
    print(n)

print_numbers(5)

'''
Use recursion when a problem can be broken into smaller subproblems (like trees or factorials),
and iteration when repetitive tasks can be solved efficiently using loops with less memory overhead.

'''
