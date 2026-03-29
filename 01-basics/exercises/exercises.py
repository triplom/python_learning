# Exercises — Module 01 Basics
# Solutions follow each exercise (hidden behind a function so you can try first)

# ─── Exercise 1 ───────────────────────────────────────────────────────────────
# Given a string with your full name, print:
# - The full name in uppercase
# - The number of characters (excluding spaces)
# - The initials (e.g., "John Paul Smith" → "J.P.S.")
# ─────────────────────────────────────────────────────────────────────────────
def ex1():
    full_name = "John Paul Smith"
    print(full_name.upper())
    print(len(full_name.replace(" ", "")))
    initials = ".".join(part[0] for part in full_name.split()) + "."
    print(initials)


# ─── Exercise 2 ───────────────────────────────────────────────────────────────
# A store sells items at R$49.99. Calculate:
# - Price after 10% discount
# - Price after 7.5% tax applied to discounted price
# - Total if buying 3 units
# ─────────────────────────────────────────────────────────────────────────────
def ex2():
    price = 49.99
    discounted = price * 0.90
    with_tax = discounted * 1.075
    total = with_tax * 3
    print(f"Discounted: R${discounted:.2f}")
    print(f"With tax:   R${with_tax:.2f}")
    print(f"3 units:    R${total:.2f}")


# ─── Exercise 3 ───────────────────────────────────────────────────────────────
# Check if a word is a palindrome (reads the same forwards and backwards)
# Test with: "racecar", "hello", "madam", "python"
# ─────────────────────────────────────────────────────────────────────────────
def ex3():
    words = ["racecar", "hello", "madam", "python"]
    for word in words:
        is_palindrome = word == word[::-1]
        print(f"'{word}' → palindrome: {is_palindrome}")


# ─── Exercise 4 ───────────────────────────────────────────────────────────────
# Temperature converter
# Convert 0, 20, 37, 100 degrees Celsius to Fahrenheit and Kelvin
# F = C * 9/5 + 32 ; K = C + 273.15
# ─────────────────────────────────────────────────────────────────────────────
def ex4():
    temps_c = [0, 20, 37, 100]
    print(f"{'°C':>6} {'°F':>8} {'K':>8}")
    print("-" * 26)
    for c in temps_c:
        f = c * 9 / 5 + 32
        k = c + 273.15
        print(f"{c:>6} {f:>8.2f} {k:>8.2f}")


# Run all exercises
if __name__ == "__main__":
    print("─── Exercise 1 ───")
    ex1()
    print("\n─── Exercise 2 ───")
    ex2()
    print("\n─── Exercise 3 ───")
    ex3()
    print("\n─── Exercise 4 ───")
    ex4()
