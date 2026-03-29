# OOP — Inheritance
# Course 4 §11 · GeeksForGeeks OOP

# ═══════════════════════════════════════
#  SINGLE INHERITANCE
# ═══════════════════════════════════════


class Animal:
    """Base (parent) class."""

    def __init__(self, name, sound):
        self.name = name
        self.sound = sound

    def speak(self):
        return f"{self.name} says {self.sound}"

    def __str__(self):
        return f"{self.__class__.__name__}({self.name!r})"


class Dog(Animal):
    """Child class inherits from Animal."""

    def __init__(self, name, breed):
        super().__init__(name, "Woof")  # call parent __init__
        self.breed = breed

    def fetch(self, item):
        return f"{self.name} fetches the {item}!"


class Cat(Animal):
    def __init__(self, name, indoor=True):
        super().__init__(name, "Meow")
        self.indoor = indoor

    def purr(self):
        return f"{self.name} purrs..."


dog = Dog("Buddy", "Labrador")
cat = Cat("Whiskers")

print(dog.speak())  # inherited from Animal
print(dog.fetch("ball"))
print(cat.speak())
print(cat.purr())

# isinstance / issubclass
print(isinstance(dog, Dog))  # True
print(isinstance(dog, Animal))  # True — Dog IS-A Animal
print(issubclass(Dog, Animal))  # True

# ═══════════════════════════════════════
#  MULTILEVEL INHERITANCE
# ═══════════════════════════════════════


class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def description(self):
        return f"{self.year} {self.make} {self.model}"


class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors

    def info(self):
        return f"{self.description()} — {self.doors} doors"


class ElectricCar(Car):
    def __init__(self, make, model, year, doors, battery_kwh):
        super().__init__(make, model, year, doors)
        self.battery_kwh = battery_kwh

    def range_estimate(self):
        # rough estimate: 6 km per kWh
        return self.battery_kwh * 6

    def info(self):
        return f"{super().info()}, {self.battery_kwh}kWh battery, ~{self.range_estimate()}km range"


ev = ElectricCar("Tesla", "Model 3", 2024, 4, 75)
print(ev.info())
print(ev.description())  # from Vehicle, 2 levels up

# ═══════════════════════════════════════
#  MULTIPLE INHERITANCE
# ═══════════════════════════════════════


class Flyable:
    def fly(self):
        return f"{self.__class__.__name__} is flying"


class Swimmable:
    def swim(self):
        return f"{self.__class__.__name__} is swimming"


class Duck(Animal, Flyable, Swimmable):
    def __init__(self, name):
        super().__init__(name, "Quack")


donald = Duck("Donald")
print(donald.speak())
print(donald.fly())
print(donald.swim())

# MRO — Method Resolution Order
print(Duck.__mro__)

# ═══════════════════════════════════════
#  METHOD OVERRIDING
# ═══════════════════════════════════════


class Shape:
    def area(self):
        return 0

    def describe(self):
        return f"I am a {self.__class__.__name__} with area {self.area():.2f}"


class Rectangle(Shape):
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def area(self):  # overrides Shape.area()
        return self.w * self.h


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


shapes = [Rectangle(4, 5), Triangle(3, 6), Rectangle(10, 2)]
for shape in shapes:
    print(shape.describe())

# --- LAB EXERCISES ---
# 1. Create a hierarchy: Person → Employee → Manager.
#    - Person: name, age
#    - Employee: adds company, salary; method give_raise(pct)
#    - Manager: adds team (list of Employee), method team_total_salary()
# 2. Create Instrument → StringInstrument, WindInstrument.
#    Each should override a play() method describing how it makes sound.
