# OOP Cheatsheet

## Class Definition

```python
class Animal:
    # Class attribute — shared by all instances
    kingdom = "Animalia"

    def __init__(self, name, sound):
        # Instance attributes — unique per object
        self.name = name
        self._sound = sound        # _ = protected (convention)
        self.__secret = "hidden"   # __ = private (name-mangled)

    def speak(self):
        return f"{self.name} says {self._sound}"

    @property
    def sound(self):              # getter
        return self._sound

    @sound.setter
    def sound(self, value):       # setter with validation
        self._sound = value.upper()

    @classmethod
    def create(cls, name):        # alternative constructor
        return cls(name, "...")

    @staticmethod
    def is_valid(name):           # utility — no self/cls
        return isinstance(name, str) and len(name) > 0

    def __str__(self):            # print(obj)
        return f"Animal({self.name!r})"

    def __repr__(self):           # repr(obj) — developer
        return f"Animal(name={self.name!r}, sound={self._sound!r})"

    def __eq__(self, other):
        return self.name == other.name

    def __lt__(self, other):      # enables sorting
        return self.name < other.name
```

## Inheritance

```python
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "Woof")   # call parent __init__
        self.breed = breed

    def speak(self):                     # override parent method
        base = super().speak()           # call parent version
        return f"{base}! I am a {self.breed}."

# isinstance / issubclass
isinstance(dog, Dog)       # True
isinstance(dog, Animal)    # True (Dog IS-A Animal)
issubclass(Dog, Animal)    # True
Dog.__mro__                # Method Resolution Order
```

## Multiple Inheritance

```python
class Flyable:
    def fly(self): return "flying"

class Swimmable:
    def swim(self): return "swimming"

class Duck(Animal, Flyable, Swimmable):
    def __init__(self, name):
        super().__init__(name, "Quack")
```

## Abstraction (ABCs)

```python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self) -> float: ...    # must be implemented by subclasses

    @abstractmethod
    def perimeter(self) -> float: ...

    def describe(self):             # concrete method — available to all
        return f"area={self.area():.2f}"

class Circle(Shape):
    def __init__(self, r): self.r = r
    def area(self): return 3.14159 * self.r ** 2
    def perimeter(self): return 2 * 3.14159 * self.r
```

## Four Pillars Quick Reference

| Pillar | Python feature | Example |
|--------|---------------|---------|
| **Encapsulation** | `__private`, `@property` | restrict access to balance |
| **Inheritance** | `class Child(Parent)` | Dog extends Animal |
| **Polymorphism** | method overriding, duck typing | speak() per species |
| **Abstraction** | `ABC`, `@abstractmethod` | Shape.area() interface |

## Dunder Methods

```python
__init__      # constructor
__str__       # str(obj) / print(obj)
__repr__      # repr(obj) — unambiguous
__len__       # len(obj)
__eq__        # obj == other
__lt__        # obj < other  (enables sorted())
__add__       # obj + other
__mul__       # obj * scalar
__contains__  # item in obj
__iter__      # for x in obj:
__next__      # next(obj)
__getitem__   # obj[key]
__setitem__   # obj[key] = val
__enter__/__exit__  # with statement (context manager)
```
