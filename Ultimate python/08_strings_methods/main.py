
s = "hello Python 123"

# 1. Case conversion
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
print(s.swapcase())
print(s.casefold())

# 2. Searching
print(s.find("Python"))
print(s.rfind("o"))
print(s.index("h"))
print(s.rindex("h"))
print(s.count("o"))

# 3. Checking methods
print(s.isalpha())
print(s.isdigit())
print(s.isdecimal())
print(s.isnumeric())
print(s.isalnum())
print(s.islower())
print(s.isupper())
print(s.istitle())
print(s.isspace())
print(s.isascii())
print(s.isidentifier())
print(s.isprintable())

# 4. Removing whitespace
print(s.strip())
print(s.lstrip())
print(s.rstrip())

# 5. Replacing
print(s.replace("Python", "World"))
print(s.expandtabs(4))

# 6. Splitting and joining
print(s.split())
print(s.rsplit())
print(s.splitlines())
print(s.partition("Python"))
print(s.rpartition("o"))
print("-".join(s.split()))

# 7. Alignment and padding
print(s.center(25, "-"))
print(s.ljust(25, "-"))
print(s.rjust(25, "-"))
print(s.zfill(25))

# 8. Prefix and suffix
print(s.startswith("hello"))
print(s.endswith("123"))
print(s.removeprefix("hello "))
print(s.removesuffix("123"))

# 9. Translation
table = str.maketrans("hello", "HELLO")
print(s.translate(table))

# 10. Formatting
print("{}".format(s))
print("{text}".format_map({"text": s}))

# 11. Other operations
print(len(s))
print(s[0])
print(s[0:5])
print("Python" in s)
print(s + "!")
print(s * 2)


'''
Mostly used methods :
Case: upper(), lower(), title(), capitalize(), swapcase(), casefold()
Search: find(), rfind(), index(), rindex(), count()
Check: isalpha(), isdigit(), isalnum(), islower(), isupper()
Trim: strip(), lstrip(), rstrip()
Modify: replace(), translate()
Split/join: split(), rsplit(), splitlines(), join()
Format: format(), format_map()
Align: center(), ljust(), rjust(), zfill()
'''
