import math
import unittest
from shapes import Circle, Triangle


class TestShapes(unittest.TestCase):

    def test_circle_area(self):
        circle = Circle(5)
        self.assertAlmostEqual(circle.area(), math.pi * 25)

    def test_triangle_area(self):
        triangle = Triangle(3, 4, 5)
        self.assertAlmostEqual(triangle.area(), 6)

    def test_right_angle_triangle(self):
        triangle = Triangle(3, 4, 5)
        self.assertTrue(triangle.is_right_angle())

    def test_not_right_angle_triangle(self):
        triangle = Triangle(3, 4, 6)
        self.assertFalse(triangle.is_right_angle())


if __name__ == "__main__":
    unittest.main()
