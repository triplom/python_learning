# Numbers and Math
# Course 2 §2 · Course 4 §4

import math

# --- Integer and float ---
x = 10
y = 3
print(x + y)  # 13   addition
print(x - y)  # 7    subtraction
print(x * y)  # 30   multiplication
print(x / y)  # 3.333...  true division (always float)
print(x // y)  # 3    floor division
print(x % y)  # 1    modulo (remainder)
print(x**y)  # 1000 exponentiation

# --- Float precision ---
print(0.1 + 0.2)  # 0.30000000000000004 — float imprecision
print(round(0.1 + 0.2, 2))  # 0.3

# --- abs, min, max, round ---
print(abs(-42))  # 42
print(min(3, 1, 4, 1, 5))  # 1
print(max(3, 1, 4, 1, 5))  # 5
print(round(3.14159, 3))  # 3.142

# --- math module ---
print(math.sqrt(16))  # 4.0
print(math.pi)  # 3.141592653589793
print(math.ceil(4.2))  # 5  (round up)
print(math.floor(4.8))  # 4  (round down)
print(math.factorial(5))  # 120
print(math.log(100, 10))  # 2.0  log base 10

# --- Augmented assignment ---
count = 0
count += 1  # count = count + 1
count *= 3
print(count)  # 3

# --- Type interactions ---
result = 5 + 2.0  # int + float → float
print(result, type(result))

# --- LAB EXERCISES ---
# 1. Calculate the area and perimeter of a rectangle (length=15, width=8).
# 2. A product costs R$129.90. After 15% discount, what is the final price?
# 3. Is 17 prime? Write a check using the % operator.
# 4. What is the hypotenuse of a right triangle with legs 3 and 4? (Pythagorean theorem)
