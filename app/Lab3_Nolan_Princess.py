
from math import pi

def circle_area(r):
    if isinstance(r, (int, float)) and r >= 0:
        return pi * (r ** 2)
    else:
        raise ValueError("Invalid radius. Must be a non-negative number.")


def trapezium_area(a, b, h):
    #Calculate the area of a trapezium given the lengths of its two parallel sides and height.
    if all(isinstance(x, (int, float)) and x >= 0 for x in [a, b, h]):
        return 0.5 * (a + b) * h
    else:
        raise ValueError("Invalid inputs. a, b, and h must be non-negative numbers.")

def ellipse_area(a, b):
    ##Calculate the area of an ellipse given its semi-major and semi-minor axes.
    if all(isinstance(x, (int, float)) and x >= 0 for x in [a, b]):
        return pi * a * b
    else:
        raise ValueError("Invalid inputs. a and b must be non-negative numbers.")


def rhombus_area(d1, d2):
    ##Calculate the area of a rhombus given its diagonals.
    if all(isinstance(x, (int, float)) and x >= 0 for x in [d1, d2]):
     return 0.5 * d1 * d2
    else:
        raise ValueError("Invalid inputs. d1 and d2 must be non-negative numbers.")

