# Module 05 — OOP

Object-Oriented Programming in Python, covering all four pillars.

**Course refs:** Course 4 §11 · GeeksForGeeks Python OOP Concepts  
**GFG reference:** https://www.geeksforgeeks.org/python-oops-concepts/

---

## Files

| File | Topic |
|------|-------|
| `classes_basics.py` | Classes, objects, `__init__`, class vs instance attrs, dunder methods |
| `inheritance.py` | Single, multilevel, multiple inheritance, `super()`, MRO, overriding |
| `encapsulation.py` | Private/protected attrs, `@property`, ABC, abstract methods |
| `polymorphism.py` | Method overriding, duck typing, operator overloading |
| `projects/library_system.py` | Mini-project: library management with OOP |

---

## The Four Pillars (GFG)

| Pillar | What it means | Python mechanism |
|--------|---------------|-----------------|
| **Encapsulation** | Bundle data + methods; control access | `__private`, `@property` |
| **Inheritance** | Child class acquires parent's attrs/methods | `class Child(Parent)` |
| **Polymorphism** | Same interface, different behavior | Method overriding, duck typing |
| **Abstraction** | Hide implementation, expose interface | `ABC`, `@abstractmethod` |

---

## Quick Reference

```python
# Class definition
class MyClass(ParentClass):
    class_var = "shared"

    def __init__(self, x):
        self.x = x          # instance attribute

    @property
    def value(self):
        return self.x

    @value.setter
    def value(self, v):
        self.x = v

    @classmethod
    def create(cls, ...):   # alternative constructor
        ...

    @staticmethod
    def helper(...):        # utility, no self or cls
        ...

    def __str__(self):      # print(obj)
        return f"MyClass({self.x})"

    def __repr__(self):     # repr(obj), debugging
        return f"MyClass(x={self.x!r})"
```
