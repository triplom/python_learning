# Advanced Python — Comprehensions, Generators
# Course 1 §4

# ═══════════════════════════════════════
#  LIST COMPREHENSIONS
# ═══════════════════════════════════════
# [expression for item in iterable if condition]

numbers = range(1, 11)

squares = [x**2 for x in numbers]
print(squares)

evens = [x for x in numbers if x % 2 == 0]
print(evens)

even_squares = [x**2 for x in numbers if x % 2 == 0]
print(even_squares)

# With function call
words = ["hello", "world", "python"]
upper = [w.upper() for w in words]
lengths = [len(w) for w in words]
print(upper, lengths)

# Nested list comprehension (flatten 2D matrix)
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [val for row in matrix for val in row]
print(flat)

# ═══════════════════════════════════════
#  DICT COMPREHENSIONS
# ═══════════════════════════════════════
# {key: value for item in iterable if condition}

names = ["Alice", "Bob", "Carol"]
scores = [92, 85, 78]

score_map = {name: score for name, score in zip(names, scores)}
print(score_map)

passing = {k: v for k, v in score_map.items() if v >= 90}
print(passing)

# Invert a dict
inverted = {v: k for k, v in score_map.items()}
print(inverted)

# ═══════════════════════════════════════
#  SET COMPREHENSIONS
# ═══════════════════════════════════════
words_text = "the quick brown fox jumps over the lazy dog"
unique_lengths = {len(w) for w in words_text.split()}
print(sorted(unique_lengths))

# ═══════════════════════════════════════
#  GENERATORS
# ═══════════════════════════════════════
# Like list comprehensions, but lazy — compute one item at a time.
# Memory efficient for large sequences.

# Generator expression (parentheses, not brackets)
gen = (x**2 for x in range(1_000_000))  # no memory allocated yet
print(next(gen))  # 0
print(next(gen))  # 1

# Sum without storing entire list in memory
total = sum(x**2 for x in range(1000))
print(total)


# Generator function — uses yield
def fibonacci():
    a, b = 0, 1
    while True:  # infinite generator
        yield a
        a, b = b, a + b


fib = fibonacci()
first_10 = [next(fib) for _ in range(10)]
print(first_10)


def countdown(n):
    while n > 0:
        yield n
        n -= 1


for val in countdown(5):
    print(val, end=" ")
print()

# ═══════════════════════════════════════
#  ENUMERATE, ZIP, SORTED, REVERSED
# ═══════════════════════════════════════

data = [("Bob", 85), ("Alice", 92), ("Carol", 78)]

# Sort by score descending
ranked = sorted(data, key=lambda x: x[1], reverse=True)
for rank, (name, score) in enumerate(ranked, start=1):
    print(f"{rank}. {name}: {score}")

# reversed()
for x in reversed(range(5)):
    print(x, end=" ")
print()

# --- LAB EXERCISES ---
# 1. Use a list comprehension to generate all Pythagorean triples (a,b,c)
#    where a,b,c <= 20 and a < b.
# 2. Write a generator function primes() that yields prime numbers indefinitely.
#    Print the first 20 primes.
# 3. Use a dict comprehension to build a frequency map from a list of words.
# 4. Compare memory usage: list vs generator for squares of 1 to 1,000,000.
#    Use sys.getsizeof() to measure.
