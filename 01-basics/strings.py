# Strings
# Course 2 §2 · Course 4 §3

# --- Creation ---
s1 = "Hello"
s2 = "World"
s3 = """Multi
line
string"""
print(s1, s2)
print(s3)

# --- Concatenation and repetition ---
greeting = s1 + ", " + s2 + "!"
print(greeting)
print("-" * 30)

# --- Indexing and slicing ---
word = "Python"
print(word[0])  # P  (first char)
print(word[-1])  # n  (last char)
print(word[0:3])  # Pyt  (index 0,1,2)
print(word[2:])  # thon
print(word[:4])  # Pyth
print(word[::-1])  # nohtyP  (reversed)

# --- String methods ---
text = "  Hello, Python World!  "
print(text.strip())  # remove surrounding whitespace
print(text.lower())
print(text.upper())
print(text.title())
print(text.replace("Python", "Beautiful"))
print(text.split(","))  # ['  Hello', ' Python World!  ']
print("python" in text.lower())  # True

# --- f-strings (Python 3.6+) ---
name = "Maria"
age = 28
print(f"My name is {name} and I am {age} years old.")
print(f"Next year I will be {age + 1}.")
print(f"Pi is approximately {3.14159:.2f}")  # 2 decimal places

# --- Useful string functions ---
print(len("Hello"))  # 5
print("abc".startswith("a"))  # True
print("hello".capitalize())  # Hello
print("a,b,c".split(","))  # ['a', 'b', 'c']
print("-".join(["a", "b", "c"]))  # a-b-c
print("hello".find("ll"))  # 2

# --- LAB EXERCISES ---
# 1. Take your full name as a string. Print: first name, last name, initials.
# 2. Count how many times the letter 'a' appears in "banana".
# 3. Reverse the string "racecar". Is it a palindrome?
# 4. Format a sentence: "Product: {name}, Price: R${price:.2f}, In stock: {qty} units"
