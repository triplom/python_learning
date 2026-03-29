# OOP — Classes and Objects
# Course 4 §11 · GeeksForGeeks OOP Concepts

# ═══════════════════════════════════════
#  CLASS BASICS
# ═══════════════════════════════════════


class Dog:
    """Blueprint for a dog object."""

    species = "Canis lupus familiaris"  # class attribute (shared by all instances)

    def __init__(self, name, age, breed):
        """Constructor — runs when object is created."""
        self.name = name  # instance attributes (unique per object)
        self.age = age
        self.breed = breed

    def bark(self):
        return f"{self.name} says: Woof!"

    def info(self):
        return f"{self.name} ({self.breed}), {self.age} year(s) old"

    def __str__(self):
        """String representation — used by print()."""
        return f"Dog({self.name!r}, age={self.age})"

    def __repr__(self):
        return f"Dog(name={self.name!r}, age={self.age}, breed={self.breed!r})"


# Creating objects (instances)
dog1 = Dog("Buddy", 3, "Labrador")
dog2 = Dog("Rex", 5, "German Shepherd")

print(dog1)  # uses __str__
print(dog1.bark())
print(dog2.info())

# Class vs instance attribute
print(Dog.species)
print(dog1.species)

# Modify instance attribute
dog1.age = 4
print(dog1.age)  # 4
print(dog2.age)  # 5 — unaffected

# ═══════════════════════════════════════
#  CLASS METHODS AND STATIC METHODS
# ═══════════════════════════════════════


class Circle:
    PI = 3.14159265

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        """Instance method — uses self."""
        return self.PI * self.radius**2

    def perimeter(self):
        return 2 * self.PI * self.radius

    @classmethod
    def from_diameter(cls, diameter):
        """Class method — alternative constructor."""
        return cls(diameter / 2)

    @staticmethod
    def is_valid_radius(r):
        """Static method — no access to class or instance."""
        return r > 0


c1 = Circle(5)
print(f"Area: {c1.area():.2f}")
print(f"Perimeter: {c1.perimeter():.2f}")

c2 = Circle.from_diameter(10)  # radius = 5
print(f"Area from diameter: {c2.area():.2f}")

print(Circle.is_valid_radius(-1))  # False

# ═══════════════════════════════════════
#  __dunder__ METHODS (magic methods)
# ═══════════════════════════════════════


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

    def __len__(self):
        return 2  # 2D vector

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return f"Vector({self.x}, {self.y})"


v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)  # Vector(4, 6)
print(v1 * 3)  # Vector(3, 6)
print(len(v1))  # 2
print(v1 == Vector(1, 2))  # True

# --- LAB EXERCISES ---
# 1. Create a BankAccount class with: balance, deposit(amount), withdraw(amount),
#    get_balance(). Prevent withdrawing more than available.
# 2. Create a Rectangle class with width and height. Add methods:
#    area(), perimeter(), is_square(), and __str__.
# 3. Add a __lt__ method to Rectangle so you can sort a list of rectangles by area.
