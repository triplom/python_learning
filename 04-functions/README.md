# Module 04 — Functions

Covers function definitions, parameters, scope, lambda, map, filter, reduce, zip, and enumerate.

**Course refs:** Course 1 §3–4 · Course 4 §10

---

## Files

| File | Topic |
|------|-------|
| `basics.py` | def, return, default params, *args, **kwargs, recursion |
| `lambda_map_filter.py` | lambda, map, filter, reduce, zip, enumerate |
| `project_pipeline.py` | Mini-project: functional data pipeline |

## Key Concepts

- Functions are **first-class objects** in Python — they can be passed as arguments
- `lambda x: expr` — anonymous function for short inline logic
- `map(fn, iterable)` — apply fn to every element → returns iterator
- `filter(fn, iterable)` — keep elements where fn(x) is True
- `reduce(fn, iterable)` — collapse to single value (requires `functools`)
- `zip(a, b)` — pair elements from two iterables
- `enumerate(iterable)` — iterate with index and value
