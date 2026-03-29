# While Loops
# Course 4 §7

# --- Basic while ---
count = 0
while count < 5:
    print(count)
    count += 1

# --- break — exit loop early ---
n = 0
while True:  # infinite loop
    if n == 5:
        break
    print(n)
    n += 1

# --- continue — skip iteration ---
for i in range(10):
    if i % 2 == 0:
        continue  # skip even numbers
    print(i, end=" ")
print()

# --- while with user input (sentinel loop) ---
# Uncomment to run interactively:
# total = 0
# while True:
#     entry = input("Enter a number (or 'done' to stop): ")
#     if entry.lower() == "done":
#         break
#     total += float(entry)
# print(f"Total: {total}")

# --- while else ---
x = 1
while x < 5:
    print(x)
    x += 1
else:
    print("while finished normally")

# --- Practical: countdown timer simulation ---
import time

seconds = 5
print("Countdown:")
while seconds > 0:
    print(f"  {seconds}...")
    seconds -= 1
    # time.sleep(1)   # uncomment for real countdown
print("Go!")

# --- Practical: number guessing game logic ---
import random

secret = random.randint(1, 10)
attempts = 0
found = False

# Simulate fixed guesses for demo (remove and use input() for real game)
guesses = [3, 7, secret]  # last guess always wins in demo
for guess in guesses:
    attempts += 1
    if guess == secret:
        print(f"Correct! Secret was {secret}. Found in {attempts} attempt(s).")
        found = True
        break
    elif guess < secret:
        print(f"Guess {guess}: Too low")
    else:
        print(f"Guess {guess}: Too high")

if not found:
    print(f"Out of guesses. Secret was {secret}.")

# --- LAB EXERCISES ---
# 1. Use a while loop to print all powers of 2 that are less than 1000.
# 2. Implement a simple login system: 3 attempts max with password "python123".
# 3. Use a while loop to reverse a number (e.g., 12345 → 54321) without converting to string.
