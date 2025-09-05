import pytest
from geometry_calculator import Triangle



class TestTriangle:
    """Тесты класса Triangle"""

    def test_triangle_creation_valid(self):
        """Test valid triangle creation"""
        triangle = Triangle(3.0, 4.0, 5.0)
        assert triangle.sides == [3.0, 4.0, 5.0]

    def test_triangle_creation_invalid(self):
        """Test triangle with invalid sides"""
        # Negative sides
        with pytest.raises(ValueError):
            Triangle(-3, 4, 5)

        # Invalid triangle
        with pytest.raises(ValueError):
            Triangle(1, 1, 3)

        # Zero sides
        with pytest.raises(ValueError):
            Triangle(0, 4, 5)

    def test_triangle_area(self):
        """Test triangle area calculation"""
        test_cases = [
            ((3, 4, 5), 6.0),
            ((5, 5, 5), 10.8253),
            ((6, 8, 10), 24.0),
        ]

        for sides, expected_area in test_cases:
            triangle = Triangle(*sides)
            assert triangle.area() == pytest.approx(expected_area, rel=1e-3)

    def test_triangle_right_angled(self):
        """Test right-angled detection"""
        right_triangles = [(3, 4, 5), (5, 12, 13), (6, 8, 10)]
        non_right_triangles = [(2, 3, 4), (5, 5, 5), (3, 3, 5)]

        for sides in right_triangles:
            triangle = Triangle(*sides)
            assert triangle.is_right_triangle()

        for sides in non_right_triangles:
            triangle = Triangle(*sides)
            assert not triangle.is_right_triangle()
