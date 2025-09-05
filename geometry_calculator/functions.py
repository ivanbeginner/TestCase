from geometry_calculator.base.base import Shape



def calculate_area(*args) -> float:
    shape = Shape.create(*args)
    return shape.area()

def is_right_triangle(*args)->float:
    shape = Shape.create(*args)
    return shape.is_right_triangle()

