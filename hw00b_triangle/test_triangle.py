import unittest
from triangle import classify_triangle

class TestTriangle(unittest.TestCase):
    def test_equilateral(self):
        self.assertEqual(classify_triangle(5, 5, 5), "equilateral triangle")

    def test_isosceles(self):
        self.assertEqual(classify_triangle(5, 5, 8), "isosceles triangle")
        self.assertEqual(classify_triangle(5, 8, 5), "isosceles triangle")
        self.assertEqual(classify_triangle(8, 5, 5), "isosceles triangle")

    def test_scalene(self):
        self.assertEqual(classify_triangle(4, 5, 6), "scalene triangle")

    def test_right_scalene(self):
        self.assertEqual(classify_triangle(3, 4, 5), "scalene triangle (right)")
        self.assertEqual(classify_triangle(5, 12, 13), "scalene triangle (right)")

    def test_right_isosceles(self):
        # isosceles right triangle: legs equal, hyp = leg*sqrt(2)
        leg = 1.0
        hyp = (2 ** 0.5) * leg
        self.assertEqual(classify_triangle(leg, leg, hyp), "isosceles triangle (right)")

    def test_invalid(self):
        self.assertEqual(classify_triangle(0, 1, 1), "not a triangle")
        self.assertEqual(classify_triangle(-1, 2, 3), "not a triangle")
        self.assertEqual(classify_triangle(1, 2, 3), "not a triangle")  # degenerate

    def test_non_numeric(self):
        self.assertEqual(classify_triangle("a", 2, 3), "not a triangle")

if __name__ == '__main__':
    unittest.main()
