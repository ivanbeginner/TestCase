import pytest
from geometry_calculator import Circle, Triangle
from geometry_calculator.base.base import Shape

class TestRegistration:
    """Тесты авторегистрации форм"""

    def test_registry_content(self):
        """Test registry content"""
        registry = Shape._registry
        assert registry[1] == Circle
        assert registry[3] == Triangle

    def test_circle_registered(self):
        """Test Circle registration"""
        assert 1 in Shape._registry
        assert Shape._registry[1].__name__ == 'Circle'

    def test_triangle_registered(self):
        """Test Triangle registration"""
        assert 3 in Shape._registry
        assert Shape._registry[3].__name__ == 'Triangle'

    def test_argument_count_detection(self):
        """Test automatic argument count detection"""
        circle_args = Circle._get_expected_arg_count()
        triangle_args = Triangle._get_expected_arg_count()

        assert circle_args == 1
        assert triangle_args == 3