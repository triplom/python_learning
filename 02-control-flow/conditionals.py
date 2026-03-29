# Conditionals
# Course 2 §4 · Course 4 §6

# --- Basic if/else ---
age = 20
if age >= 18:
    print("Adult")
else:
    print("Minor")

# --- if/elif/else ---
score = 75
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"
print(f"Score {score} → Grade {grade}")

# --- Comparison operators ---
# ==  !=  <  >  <=  >=
print(5 == 5)  # True
print(5 != 3)  # True
print(3 < 5)  # True

# --- Logical operators: and, or, not ---
x = 15
if x > 10 and x < 20:
    print("x is between 10 and 20")

if x < 0 or x > 100:
    print("x is out of normal range")
else:
    print("x is in normal range")

print(not True)  # False

# --- Truthy / Falsy ---
# Falsy: 0, "", [], {}, None, False
# Truthy: everything else
if "":
    print("empty string is truthy")  # won't print
if "hello":
    print("non-empty string is truthy")  # prints

# --- Ternary (one-liner if) ---
status = "even" if 10 % 2 == 0 else "odd"
print(status)

# --- Nested if ---
num = 7
if num > 0:
    if num % 2 == 0:
        print("Positive even")
    else:
        print("Positive odd")
else:
    print("Non-positive")

# --- LAB EXERCISES ---
# 1. Ask the user for a temperature. Print: "Hot" (>30), "Warm" (20-30),
#    "Cool" (10-20), "Cold" (<10).
# 2. Ask for a year. Print whether it is a leap year.
#    (Leap year: divisible by 4, except centuries unless divisible by 400)
# 3. Ask for 3 numbers. Print the largest without using max().
