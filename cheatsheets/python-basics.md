# Python Basics Cheatsheet

## Variables & Types

```python
x = 42          # int
y = 3.14        # float
s = "hello"     # str
b = True        # bool
n = None        # NoneType

type(x)         # <class 'int'>
int("42")       # cast str → int
float(3)        # cast int → float
str(42)         # cast int → str
```

## Strings

```python
s = "Hello, World!"
s.upper()          # 'HELLO, WORLD!'
s.lower()          # 'hello, world!'
s.strip()          # remove whitespace
s.split(",")       # ['Hello', ' World!']
",".join(["a","b"]) # 'a,b'
s[0]               # 'H'
s[-1]              # '!'
s[0:5]             # 'Hello'
s[::-1]            # reversed
len(s)             # 13
f"Hi {name}"       # f-string
f"{pi:.2f}"        # 2 decimal places
"hi" in s          # membership
s.replace("l","r") # 'Herro, Worrd!'
s.startswith("H")  # True
s.find("o")        # 4
```

## Numbers & Math

```python
10 / 3    # 3.333  true division
10 // 3   # 3      floor division
10 % 3    # 1      modulo
2 ** 8    # 256    power
abs(-5)   # 5
round(3.14159, 2)  # 3.14
min(1,2,3)  # 1
max(1,2,3)  # 3

import math
math.sqrt(16)    # 4.0
math.pi          # 3.14159...
math.ceil(4.1)   # 5
math.floor(4.9)  # 4
math.factorial(5) # 120
```

## Input / Output

```python
name = input("Enter name: ")   # always returns str
age  = int(input("Age: "))     # cast immediately
print(f"Hello {name}, age {age}")
print(x, y, sep=", ", end="\n")
```

## Conditionals

```python
if x > 0:
    print("positive")
elif x == 0:
    print("zero")
else:
    print("negative")

# Ternary
label = "even" if x % 2 == 0 else "odd"
```

## Loops

```python
for i in range(5):        # 0 1 2 3 4
    print(i)

for i, v in enumerate(lst):
    print(i, v)

while x > 0:
    x -= 1

break     # exit loop
continue  # skip to next iteration
```

## Lists

```python
lst = [1, 2, 3]
lst.append(4)       # [1,2,3,4]
lst.insert(0, 0)    # insert at index
lst.remove(2)       # remove first 2
lst.pop()           # remove & return last
lst.sort()
lst.reverse()
lst[1:3]            # slice
lst[::-1]           # reversed copy
len(lst)            # length
x in lst            # membership
sorted(lst)         # new sorted list
```

## Dicts

```python
d = {"a": 1, "b": 2}
d["c"] = 3          # add/update
d.get("x", 0)       # safe get with default
del d["a"]
d.keys()   d.values()   d.items()
for k, v in d.items(): ...
d.update({"d": 4})
d.pop("b")
```

## Sets

```python
s = {1, 2, 3}
s.add(4)
s.discard(1)      # no error if absent
s1 & s2           # intersection
s1 | s2           # union
s1 - s2           # difference
s1 ^ s2           # symmetric difference
```

## Useful Built-ins

```python
len()   type()   range()   print()   input()
int()   float()  str()     bool()    list()
dict()  set()    tuple()   sorted()  reversed()
sum()   min()    max()     abs()     round()
zip()   map()    filter()  enumerate()
```
