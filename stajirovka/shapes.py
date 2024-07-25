import math


class Shape:
    def area(self):
        raise NotImplementedError("This method should be overridden in subclasses.")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right_angle(self):
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(sides[2] ** 2, sides[0] ** 2 + sides[1] ** 2)


# Example usage:
if __name__ == "__main__":
    circle = Circle(5)
    print(f"Area of the circle: {circle.area()}")

    triangle = Triangle(3, 4, 5)
    print(f"Area of the triangle: {triangle.area()}")
    print(f"Is the triangle right-angled? {triangle.is_right_angle()}")
