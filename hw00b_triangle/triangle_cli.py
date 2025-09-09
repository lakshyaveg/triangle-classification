"""Simple CLI to classify triangles.

Usage:
    python triangle_cli.py 3 4 5
    # or run without args to be prompted
"""
import sys
from triangle import classify_triangle

def main(argv=None):
    argv = argv or sys.argv[1:]
    if len(argv) == 3:
        a, b, c = argv
    else:
        print("Enter side lengths a, b, c:")
        a = input("a: ").strip()
        b = input("b: ").strip()
        c = input("c: ").strip()
    result = classify_triangle(a, b, c)
    print(result)

if __name__ == "__main__":
    main()
