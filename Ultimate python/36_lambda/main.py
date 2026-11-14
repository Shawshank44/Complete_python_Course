'''
In Python, a lambda function is a small anonymous function defined using the lambda keyword.
It can take any number of arguments but contains only one expression.

lambda arguments: expression

'''
# 1. Lambda with one argument
square = lambda x : x * x
print(square(5))

# 2. Lambda with two arguments
add = lambda a,b : a + b
print(add(50,20))

# 3. Lambda with multiple arguments
calculate = lambda a, b, c: (a + b + c)
print(calculate(10, 20, 30))

# 4. Lambda with if-else
check = lambda x: "Even" if x % 2==0 else "Odd"
print(check(7))

# 5. Lambda function as an argument to a normal function.
def calculate(func, a, b):
    return func(a, b)
result = calculate(lambda x, y: x * y, 10, 20)
print(result)

'''
Lambda vs Normal Function
Normal function - Lambda function
Uses def - Uses lambda
Has a function name - Usually anonymous
Supports multiple statements - Supports one expression
Suitable for complex logic - Suitable for short operations

'''
