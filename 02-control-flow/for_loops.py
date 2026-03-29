# For Loops
# Course 4 §7

# --- Basic for loop ---
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# --- range() ---
for i in range(5):  # 0 1 2 3 4
    print(i, end=" ")
print()

for i in range(1, 11):  # 1 to 10
    print(i, end=" ")
print()

for i in range(0, 20, 2):  # even numbers
    print(i, end=" ")
print()

for i in range(10, 0, -1):  # countdown
    print(i, end=" ")
print()

# --- Iterating strings ---
for char in "Python":
    print(char, end="-")
print()

# --- Nested loops ---
for row in range(1, 4):
    for col in range(1, 4):
        print(f"{row * col:3}", end="")
    print()

# --- enumerate() — index + value ---
animals = ["cat", "dog", "fish"]
for i, animal in enumerate(animals):
    print(f"{i}: {animal}")

# --- Loop with accumulator ---
total = 0
for n in range(1, 101):
    total += n
print(f"Sum 1 to 100 = {total}")  # 5050

# --- for with else (runs when loop finishes normally, not via break) ---
for n in range(3):
    print(n)
else:
    print("Loop finished")

# --- LAB EXERCISES ---
# 1. Print the multiplication table for a number entered by the user (1×n to 10×n).
# 2. Sum all even numbers from 1 to 100.
# 3. Print a right-triangle pattern of * with 5 rows:
#    *
#    **
#    ***
#    ****
#    *****
# 4. Given a list of prices, print each with a 10% discount applied.
