# OOP — Encapsulation and Abstraction
# Course 4 §11 · GeeksForGeeks OOP

from abc import ABC, abstractmethod

# ═══════════════════════════════════════
#  ENCAPSULATION
# ═══════════════════════════════════════
# Bundling data + methods; restricting direct access to internals.


class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.__balance = initial_balance  # __ = private (name-mangled)
        self._transaction_log = []  # _ = protected (convention)

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.__balance += amount
        self._transaction_log.append(f"+{amount:.2f}")
        return self

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount
        self._transaction_log.append(f"-{amount:.2f}")
        return self

    @property
    def balance(self):
        """Read-only property — getter."""
        return self.__balance

    @property
    def history(self):
        return list(self._transaction_log)

    def __str__(self):
        return f"BankAccount({self.owner!r}, balance=R${self.__balance:.2f})"


account = BankAccount("Alice", 1000)
account.deposit(500).withdraw(200)  # method chaining

print(account.balance)  # 1300.0 (via property)
print(account.history)  # ['+500.00', '-200.00']
print(account)

# Direct access blocked:
# account.__balance   # AttributeError
# but name mangling allows: account._BankAccount__balance (don't do this)

# ─── @property with setter ───────────────────────────────────────────────────


class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius

    @property
    def celsius(self):
        return self._celsius

    @celsius.setter
    def celsius(self, value):
        if value < -273.15:
            raise ValueError("Temperature below absolute zero")
        self._celsius = value

    @property
    def fahrenheit(self):
        return self._celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) * 5 / 9


t = Temperature(25)
print(f"{t.celsius}°C = {t.fahrenheit}°F")

t.fahrenheit = 212
print(f"{t.celsius}°C = {t.fahrenheit}°F")

# ═══════════════════════════════════════
#  ABSTRACTION
# ═══════════════════════════════════════
# Abstract classes define an interface — subclasses must implement it.


class Shape(ABC):
    """Abstract base class — cannot be instantiated."""

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass

    def describe(self):
        """Concrete method — available to all subclasses."""
        return (
            f"{self.__class__.__name__}: "
            f"area={self.area():.2f}, perimeter={self.perimeter():.2f}"
        )


class Circle(Shape):
    PI = 3.14159265

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.PI * self.radius**2

    def perimeter(self):
        return 2 * self.PI * self.radius


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


# Shape()   # TypeError: Can't instantiate abstract class

shapes = [Circle(5), Rectangle(4, 6), Circle(3)]
for s in shapes:
    print(s.describe())

total_area = sum(s.area() for s in shapes)
print(f"Total area: {total_area:.2f}")

# --- LAB EXERCISES ---
# 1. Create an abstract class Vehicle with abstract methods fuel_type() and
#    max_speed(). Implement Car (gasoline, 200 km/h) and Bicycle (human, 30 km/h).
# 2. Refactor BankAccount to have a private __transaction_count.
#    Add a property that returns it and a class method that returns the total
#    number of accounts created (class-level counter).
