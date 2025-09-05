import math

from geometry_calculator.base.base import Shape




class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        sides = [a, b, c]
        if any(side <= 0 for side in sides):
            raise ValueError("All sides must be positive")
        if not self._is_valid_triangle(a, b, c):
            raise ValueError("Invalid triangle sides")
        self.sides = sorted(sides)
    def _is_valid_triangle(self, a: float, b: float, c: float) -> bool:
        return (a + b > c) and (a + c > b) and (b + c > a)

    def area(self) -> float:
        s = sum(self.sides) / 2
        return math.sqrt(s * (s - self.sides[0]) *
                         (s - self.sides[1]) * (s - self.sides[2]))

    def is_right_triangle(self) -> bool:
        a, b, c = self.sides
        return a** 2 + b ** 2 == c ** 2