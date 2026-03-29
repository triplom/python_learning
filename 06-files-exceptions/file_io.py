# File I/O and Exception Handling
# Course 1 §3

import os

# ═══════════════════════════════════════
#  WRITING FILES
# ═══════════════════════════════════════

# Write (overwrites if file exists)
with open("sample.txt", "w") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")
    f.write("Line 3\n")

# Append (adds to end of file)
with open("sample.txt", "a") as f:
    f.write("Line 4 (appended)\n")

# ═══════════════════════════════════════
#  READING FILES
# ═══════════════════════════════════════

# Read entire file as string
with open("sample.txt", "r") as f:
    content = f.read()
    print(content)

# Read line by line (memory efficient for large files)
with open("sample.txt", "r") as f:
    for line in f:
        print(line.strip())

# Read all lines as list
with open("sample.txt", "r") as f:
    lines = f.readlines()
    print(lines)

# readline() — one line at a time
with open("sample.txt", "r") as f:
    first = f.readline()
    second = f.readline()
    print(repr(first), repr(second))

# ═══════════════════════════════════════
#  CSV FILES
# ═══════════════════════════════════════

import csv

# Write CSV
students = [
    ["Name", "Age", "Grade"],
    ["Alice", 20, "A"],
    ["Bob", 22, "B"],
    ["Carol", 21, "A"],
]

with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(students)

# Read CSV
with open("students.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(dict(row))

# ═══════════════════════════════════════
#  EXCEPTION HANDLING
# ═══════════════════════════════════════

# Basic try/except
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"Error: {e}")


# Multiple exception types
def safe_convert(value):
    try:
        return int(value)
    except ValueError:
        print(f"Cannot convert {value!r} to int")
        return None
    except TypeError:
        print("Wrong type passed")
        return None


print(safe_convert("42"))  # 42
print(safe_convert("abc"))  # None
print(safe_convert(None))  # None


# else (runs when no exception) + finally (always runs)
def read_file_safe(path):
    try:
        f = open(path, "r")
        content = f.read()
    except FileNotFoundError:
        print(f"File not found: {path}")
        return None
    else:
        print("File read successfully")
        return content
    finally:
        print("Cleanup — always runs")
        try:
            f.close()
        except:
            pass


read_file_safe("sample.txt")
read_file_safe("nonexistent.txt")

# Common exception types
exceptions = [
    ("ZeroDivisionError", "10 / 0"),
    ("ValueError", "int('abc')"),
    ("TypeError", "'2' + 2"),
    ("IndexError", "[1,2,3][10]"),
    ("KeyError", "{}['x']"),
    ("AttributeError", "None.upper()"),
]
for name, code in exceptions:
    try:
        eval(code)
    except Exception as e:
        print(f"{name}: {e}")

# ─── Custom Exceptions ────────────────────────────────────────────────────────


class InsufficientFundsError(Exception):
    """Raised when a withdrawal exceeds available balance."""

    def __init__(self, amount, balance):
        self.amount = amount
        self.balance = balance
        super().__init__(f"Cannot withdraw {amount:.2f}: only {balance:.2f} available")


def withdraw(amount, balance):
    if amount > balance:
        raise InsufficientFundsError(amount, balance)
    return balance - amount


try:
    new_balance = withdraw(500, 200)
except InsufficientFundsError as e:
    print(e)

# Cleanup temp files
for fname in ["sample.txt", "students.csv"]:
    if os.path.exists(fname):
        os.remove(fname)

# --- LAB EXERCISES ---
# 1. Write a function that reads a CSV of products (name, price, qty),
#    computes total value per product, and writes a new CSV with a "total" column.
# 2. Create a safe_divide(a, b) function that handles ZeroDivisionError and TypeError.
# 3. Create a custom ValidationError. Write a function validate_age(age) that raises
#    it if age is not an int or is outside 0–150.
