# HW 00b — Testing Triangle Classification

This repo implements `classify_triangle(a, b, c)` and includes **unittest** tests and a small CLI.

## How to run
```bash
python triangle_cli.py 3 4 5
# -> scalene triangle (right)
```

## How to test
```bash
python -m unittest -v
```

## Function contract (what it returns)
- `equilateral triangle`
- `isosceles triangle`
- `scalene triangle`
- Appends ` (right)` when the triangle is right-angled.
- Returns `not a triangle` for invalid input.
