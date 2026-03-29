# Functions
# Course 1 §3 · Course 4 §10

# --- Basic function ---
def greet(name):
    """Return a greeting string."""
    return f"Hello, {name}!"


print(greet("Alice"))


# --- Multiple return values (tuple) ---
def min_max(numbers):
    return min(numbers), max(numbers)


lo, hi = min_max([3, 1, 4, 1, 5, 9])
print(lo, hi)


# --- Default parameters ---
def power(base, exponent=2):
    return base**exponent


print(power(3))  # 9  (exponent defaults to 2)
print(power(2, 10))  # 1024


# --- Keyword arguments ---
def describe_person(name, age, city="Unknown"):
    print(f"{name}, {age}, from {city}")


describe_person("Alice", 30, city="São Paulo")
describe_person(age=25, name="Bob")


# --- *args — variable positional arguments ---
def total(*args):
    """Sum any number of arguments."""
    return sum(args)


print(total(1, 2, 3))
print(total(10, 20, 30, 40))


# --- **kwargs — variable keyword arguments ---
def display_info(**kwargs):
    for key, value in kwargs.items():
        print(f"  {key}: {value}")


display_info(name="Alice", role="Developer", level=3)


# --- Combining: positional, *args, **kwargs ---
def full_example(required, *args, **kwargs):
    print(f"Required: {required}")
    print(f"Extra positional: {args}")
    print(f"Extra keyword: {kwargs}")


full_example("hello", 1, 2, 3, x=10, y=20)

# --- Scope: local vs global ---
count = 0  # global


def increment():
    global count  # declare intent to modify global
    count += 1


increment()
increment()
print(count)  # 2


# --- Recursion ---
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)


print(factorial(5))  # 120


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


print([fibonacci(i) for i in range(10)])

# --- LAB EXERCISES ---
# 1. Write a function is_palindrome(s) that returns True if s is a palindrome.
# 2. Write a function flatten(nested_list) that flattens one level of nesting.
# 3. Write a function word_count(text) that returns a dict of {word: count}.
# 4. Write a recursive function sum_digits(n) that sums the digits of an integer.
