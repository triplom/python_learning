# Dictionaries, Tuples, and Sets
# Course 4 §9

# ═══════════════════════════════════════
#  DICTIONARIES
# ═══════════════════════════════════════

person = {"name": "Alice", "age": 30, "city": "São Paulo"}

# --- Access ---
print(person["name"])  # Alice
print(person.get("email", "N/A"))  # N/A (safe get with default)

# --- Mutation ---
person["email"] = "alice@example.com"  # add key
person["age"] = 31  # update value
del person["city"]  # delete key

# --- Iteration ---
for key in person:
    print(key, ":", person[key])

for key, value in person.items():
    print(f"  {key}: {value}")

print(list(person.keys()))
print(list(person.values()))

# --- Dict methods ---
d = {"a": 1, "b": 2}
d.update({"b": 99, "c": 3})  # merge/update
print(d)
print(d.pop("a"))  # remove and return value

# --- Nested dicts ---
students = {
    "Alice": {"grade": "A", "score": 95},
    "Bob": {"grade": "B", "score": 82},
}
print(students["Alice"]["score"])

# ═══════════════════════════════════════
#  TUPLES
# ═══════════════════════════════════════

# Immutable ordered sequence — great for fixed data / multiple returns
coords = (10.5, -23.4)
rgb = (255, 128, 0)
single = (42,)  # trailing comma required for single-element tuple

print(coords[0])  # 10.5
# coords[0] = 5         # TypeError — tuples are immutable

# Tuple unpacking
x, y = coords
print(f"x={x}, y={y}")

lat, lon = coords
print(f"Latitude: {lat}, Longitude: {lon}")

# Named tuple (structured data without a class)
from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p = Point(3, 4)
print(p.x, p.y)

# Tuples in lists
employees = [("Alice", "Engineering", 95000), ("Bob", "Marketing", 78000)]
for name, dept, salary in employees:
    print(f"{name} ({dept}): R${salary:,}")

# ═══════════════════════════════════════
#  SETS
# ═══════════════════════════════════════

# Unordered, no duplicates — great for membership tests and set operations
primes = {2, 3, 5, 7, 11}
evens = {2, 4, 6, 8, 10}

# Deduplication
dupes = [1, 2, 2, 3, 3, 3, 4]
unique = set(dupes)
print(unique)  # {1, 2, 3, 4}

# Membership (O(1) average)
print(5 in primes)  # True

# Set operations
print(primes & evens)  # intersection: {2}
print(primes | evens)  # union
print(primes - evens)  # difference (in primes, not in evens)
print(primes ^ evens)  # symmetric difference (in one but not both)

# Mutation
primes.add(13)
primes.discard(2)  # remove if present (no error if absent)
print(primes)

# Subset / superset
a = {1, 2}
b = {1, 2, 3}
print(a.issubset(b))  # True
print(b.issuperset(a))  # True

# --- LAB EXERCISES ---
# 1. Build a dict mapping country codes to country names (at least 5 entries).
#    Ask for a code and print the full name, or "Not found".
# 2. Given two lists of student names (class A and class B), find:
#    - Students in both classes
#    - Students only in class A
#    - All unique students combined
# 3. From a list of words, count occurrences using a dict (no Counter).
#    Input: ["apple", "banana", "apple", "cherry", "banana", "apple"]
