# Variables and Data Types
# Course 2 §2 · Course 4 §2–3

# --- Variable assignment ---
name = "Alice"
age = 30
height = 1.72
is_student = True

print(name, age, height, is_student)

# --- type() ---
print(type(name))  # <class 'str'>
print(type(age))  # <class 'int'>
print(type(height))  # <class 'float'>
print(type(is_student))  # <class 'bool'>

# --- Type casting ---
x = "42"
print(type(x))  # str
x_int = int(x)
print(type(x_int))  # int

pi = 3.14159
pi_str = str(pi)
print(pi_str, type(pi_str))

# --- Multiple assignment ---
a, b, c = 1, 2, 3
print(a, b, c)

# All point to the same value
x = y = z = 0
print(x, y, z)

# --- Naming rules ---
# good_name, _private, CamelCase (classes), ALL_CAPS (constants)
MAX_SPEED = 300  # constant by convention
_internal = "private"

# --- None type ---
result = None
print(result, type(result))  # None <class 'NoneType'>

# --- LAB EXERCISES ---
# 1. Create variables for your name, birth year, and city. Print them with labels.
# 2. Swap the values of two variables without a third variable.
# 3. What is the type of: True + 1? Predict, then verify with type().
