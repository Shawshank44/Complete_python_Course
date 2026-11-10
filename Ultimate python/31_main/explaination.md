Understanding how `if __name__ == "__main__":` works. Let's execute your code step by step.

You have two Python files:

## 1. calcu.py

```
def add(a,b):    print(a+b)def sub(a,b):    print(a-b)def mul(a,b):    print(a*b)print(__name__)if __name__ == "__main__":    print("calculation started")    add(10,2)    sub(10,5)    mul(10,10)
```

## 2. main.py

```
import calcuprint("Main function started")print(__name__)calcu.add(10,5)calcu.sub(2,1)calcu.mul(10,5)
```

## Case 1: You run calcu.py directly

Command:

```
python calcu.py
```

Output:

```
__main__
calculation started
12
5
100
```

Why?

1. Python starts executing `calcu.py`.
2. It defines the three functions: `add()`, `sub()` and `mul()`.
3. It executes `print(__name__)`.
4. Since you're running `calcu.py` directly, `__name__` contains `"__main__"`.
5. The `if` condition becomes `True`.
6. Therefore, it executes the calculation code.

## Case 2: You run main.py

Command:

```
python main.py
```

Output:

```
calcu
Main function started
__main__
15
1
50
```

Now let's understand exactly what happens.

Step 1:

```
import calcu
```

Python goes to `calcu.py` and starts executing it.

Step 2:

It defines the functions:

```
def add(a,b):    print(a+b)def sub(a,b):    print(a-b)def mul(a,b):    print(a*b)
```

These functions are defined but not executed yet.

Step 3:

Python encounters:

```
print(__name__)
```

Since `calcu.py` is being imported, its `__name__` value is:

```
calcu
```

So it prints:

```
calcu
```

Step 4:

Python encounters:

```
if __name__ == "__main__":
```

Here:

```
__name__ = "calcu"
```

Therefore:

```
"calcu" == "__main__"
```

The condition is `False`.

So Python skips this entire block:

```
print("calculation started")add(10,2)sub(10,5)mul(10,10)
```

Step 5:

Python returns to `main.py` and continues executing.

```
print("Main function started")print(__name__)
```

Since `main.py` is being executed directly, its `__name__` is `"__main__"`.

Output:

```
Main function started
__main__
```

Step 6:

Now these functions are called:

```
calcu.add(10,5)calcu.sub(2,1)calcu.mul(10,5)
```

They execute normally because importing `calcu` made its functions available to `main.py`.

Output:

```
15
1
50
```

## 3. Visual understanding

This is the execution flow when you run `main.py`:

Run main.py

import calcu

Python enters calcu.py

print(name)

Output: calcu

if name == "main":

False

Skip the calculation block

Return to main.py

Execute main.py code

15, 1, 50

## 4. The most important thing to remember

You have two different `__name__` variables here:

| File     | How it's executed   | `__name__`   |
| -------- | ------------------- | ------------ |
| calcu.py | Imported by main.py | `"calcu"`    |
| main.py  | Run directly        | `"__main__"` |

One important point: Importing a Python file executes its top-level code once (unless it has already been imported and cached). The `if __name__ == "__main__":` condition doesn't prevent the entire file from executing. It only prevents the code inside that particular `if` block from executing.
