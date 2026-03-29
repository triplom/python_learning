# Lambda, Map, Filter, Reduce, Zip, Enumerate
# Course 1 §4 · Course 4 §10

from functools import reduce

# ═══════════════════════════════════════
#  LAMBDA — anonymous inline functions
# ═══════════════════════════════════════
square = lambda x: x**2
add = lambda a, b: a + b

print(square(5))  # 25
print(add(3, 4))  # 7

# Common use: sorting by key
people = [("Alice", 30), ("Bob", 25), ("Carol", 35)]
people.sort(key=lambda p: p[1])  # sort by age
print(people)

# ═══════════════════════════════════════
#  MAP — apply function to every element
# ═══════════════════════════════════════
numbers = [1, 2, 3, 4, 5]


# With named function
def double(x):
    return x * 2


doubled = list(map(double, numbers))
print(doubled)  # [2, 4, 6, 8, 10]

# With lambda (more concise)
squared = list(map(lambda x: x**2, numbers))
print(squared)

# Map over multiple iterables
a = [1, 2, 3]
b = [10, 20, 30]
sums = list(map(lambda x, y: x + y, a, b))
print(sums)  # [11, 22, 33]

# ═══════════════════════════════════════
#  FILTER — keep elements matching a condition
# ═══════════════════════════════════════
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

evens = list(filter(lambda x: x % 2 == 0, data))
print(evens)  # [2, 4, 6, 8, 10]

# Filter out empty strings
words = ["hello", "", "world", "", "python"]
non_empty = list(filter(None, words))  # None as function: truthy filter
print(non_empty)

# ═══════════════════════════════════════
#  REDUCE — collapse to a single value
# ═══════════════════════════════════════
product = reduce(lambda acc, x: acc * x, [1, 2, 3, 4, 5])
print(product)  # 120

max_val = reduce(lambda a, b: a if a > b else b, [3, 1, 4, 1, 5, 9])
print(max_val)  # 9

# ═══════════════════════════════════════
#  ZIP — combine iterables element-wise
# ═══════════════════════════════════════
names = ["Alice", "Bob", "Carol"]
scores = [92, 85, 78]
grades = ["A", "B", "C"]

for name, score, grade in zip(names, scores, grades):
    print(f"{name}: {score} ({grade})")

# Zip → dict
mapping = dict(zip(names, scores))
print(mapping)

# Unzip with *
pairs = [(1, "a"), (2, "b"), (3, "c")]
nums, letters = zip(*pairs)
print(nums)  # (1, 2, 3)
print(letters)  # ('a', 'b', 'c')

# ═══════════════════════════════════════
#  ENUMERATE — index + value
# ═══════════════════════════════════════
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits):
    print(f"{i}: {fruit}")

for i, fruit in enumerate(fruits, start=1):  # start index at 1
    print(f"{i}. {fruit}")

# ═══════════════════════════════════════
#  COMBINING
# ═══════════════════════════════════════
# Sum of squares of even numbers from 1 to 20
result = reduce(
    lambda acc, x: acc + x,
    map(lambda x: x**2, filter(lambda x: x % 2 == 0, range(1, 21))),
)
print(result)  # 1540

# --- LAB EXERCISES ---
# 1. Given prices = [29.99, 49.99, 9.99, 99.99, 14.99]:
#    - Use map() to apply 15% discount to all
#    - Use filter() to keep only prices > 20 (after discount)
#    - Use reduce() to get the total
# 2. Use zip() to create a dict from two lists: keys and values provided separately.
# 3. Use enumerate() to find the index of the maximum value in a list without max().
