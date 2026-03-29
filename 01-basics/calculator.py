# Mini-Project: Calculator
# Course 2 §3


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: division by zero"
    return a / b


def main():
    print("=" * 30)
    print("       PYTHON CALCULATOR")
    print("=" * 30)

    try:
        a = float(input("Enter first number:  "))
        b = float(input("Enter second number: "))
    except ValueError:
        print("Invalid input. Please enter numbers only.")
        return

    print("\nOperations:")
    print(f"  {a} + {b} = {add(a, b)}")
    print(f"  {a} - {b} = {subtract(a, b)}")
    print(f"  {a} * {b} = {multiply(a, b)}")
    print(f"  {a} / {b} = {divide(a, b)}")

    # Bonus: power and modulo
    print(f"  {a} ** {b} = {a**b}")
    if b != 0:
        print(f"  {a} % {b}  = {a % b}")


if __name__ == "__main__":
    main()
