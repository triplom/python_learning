# User Input
# Course 2 §2

# --- Basic input ---
name = input("Enter your name: ")
print(f"Hello, {name}!")

# --- input() always returns str — cast when needed ---
age_str = input("Enter your age: ")
age = int(age_str)
print(f"In 10 years you will be {age + 10}.")

# --- Inline cast ---
price = float(input("Enter price (R$): "))
qty = int(input("Enter quantity: "))
total = price * qty
print(f"Total: R${total:.2f}")

# --- LAB EXERCISES ---
# 1. Ask for two numbers and print their sum, difference, product, and quotient.
# 2. Ask for a name and a birth year. Calculate and print their age in 2026.
# 3. Ask for a temperature in Celsius and convert it to Fahrenheit: F = C * 9/5 + 32
