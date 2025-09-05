import math

import pytest
from geometry_calculator.shapes.circle import Circle

class TestCircle:


    def test_circle_creation_valid(self):

        circle = Circle(5.0)
        assert circle.radius == 5.0
        assert isinstance(circle, Circle)

    def test_circle_creation_invalid_radius(self):

        with pytest.raises(ValueError):
            Circle(0)
        with pytest.raises(ValueError):
            Circle(-5.0)

    def test_circle_area(self):

        test_cases = [
            (1.0, math.pi),
            (2.0, 4 * math.pi),
            (5.0, 25 * math.pi),
            (0.5, 0.25 * math.pi)
        ]

        for radius, expected_area in test_cases:
            circle = Circle(radius)
            assert circle.area() == pytest.approx(expected_area)
