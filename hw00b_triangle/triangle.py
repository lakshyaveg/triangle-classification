"""Triangle classification module.

classify_triangle(a, b, c) -> str
  Returns one of:
    - "equilateral triangle"
    - "isosceles triangle"
    - "scalene triangle"
  and appends " (right)" when the triangle is right-angled.
  Returns "not a triangle" for invalid inputs.

The function accepts ints or floats > 0.
"""

from typing import Tuple

def _is_valid(a: float, b: float, c: float) -> bool:
    # All sides must be positive
    if a <= 0 or b <= 0 or c <= 0:
        return False
    # Triangle inequality (strict)
    return a + b > c and a + c > b and b + c > a

def _is_right(a: float, b: float, c: float, *, tol: float = 1e-9) -> bool:
    # Sort sides so c is the largest
    x, y, z = sorted([a, b, c])
    return abs((x * x + y * y) - (z * z)) <= tol * (x * x + y * y + z * z)

def classify_triangle(a: float, b: float, c: float) -> str:
    """Classify a triangle by side lengths.

    Returns "not a triangle" if invalid.
    Otherwise returns one of:
      - "equilateral triangle"
      - "isosceles triangle"
      - "scalene triangle"
    and appends " (right)" when right-angled.
    """
    try:
        a = float(a)
        b = float(b)
        c = float(c)
    except (TypeError, ValueError):
        return "not a triangle"

    if not _is_valid(a, b, c):
        return "not a triangle"

    # Base classification
    if abs(a - b) < 1e-12 and abs(b - c) < 1e-12:
        kind = "equilateral triangle"
        # equilateral cannot be right-angled in Euclidean geometry
        return kind
    elif abs(a - b) < 1e-12 or abs(a - c) < 1e-12 or abs(b - c) < 1e-12:
        kind = "isosceles triangle"
    else:
        kind = "scalene triangle"

    if _is_right(a, b, c):
        kind += " (right)"
    return kind
