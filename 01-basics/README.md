# Module 01 — Python Basics

Covers variables, data types, strings, numbers, user input, and the calculator mini-project.

**Course refs:** Course 2 (Iniciantes) §1–3 · Course 4 (Zero to AI) §1–5

---

## Files

| File | Topic |
|------|-------|
| `hello_world.py` | First program, `print()`, comments |
| `variables.py` | Variables, types, `type()`, casting |
| `strings.py` | String methods, slicing, f-strings |
| `numbers.py` | int, float, operators, `math` module |
| `user_input.py` | `input()`, casting input, prompts |
| `calculator.py` | Mini-project: 4-operation calculator |
| `exercises/` | Practice problems with solutions |

## How to Run

```bash
cd 01-basics
python hello_world.py
python calculator.py
```

## Key Concepts

- Every value in Python has a **type**: `int`, `float`, `str`, `bool`
- Variables are **dynamically typed** — no declaration needed
- `type(x)` reveals the type at runtime
- String **f-strings**: `f"Hello, {name}!"`
- `input()` always returns a **string** — cast with `int()` or `float()` as needed
