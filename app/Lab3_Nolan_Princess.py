# Names: Nolan Makinen, Princess Okerulu
# Lab3_Nolan_Princess.py
# Date: 2025-02-20
# Functions to calculate the area of a circle, trapezium, ellipse, and rhombus

from math import pi

def circle_area(r):
    if not (isinstance(r, (float, int))):
        raise ValueError("Invalid circle area. Must be a float.")
    if r < 0:
        raise ValueError("Invalid circle area. Must be positive.")
    return pi * (r ** 2)

def trapezium_area(a, b, h):
    #Calculate the area of a trapezium given the lengths of its two parallel sides and height.
    if not (isinstance(a, (float, int)) and isinstance(b, (float, int)) and isinstance(h, (float, int))):
        raise ValueError("Invalid trapezium area. Must be a float.")
    if a < 0 or b < 0 or h < 0:
        raise ValueError("Invalid trapezium area. Must be positive.")
    return 0.5 * (a + b) * h

def ellipse_area(a, b):
    #Calculate the area of an ellipse given its semi-major and semi-minor axes.
    if not (isinstance(a, (float, int)) and isinstance(b, (float, int))):
        raise ValueError("Invalid ellipse area. Must be a float.")
    if a < 0 or b < 0:
        raise ValueError("Invalid ellipse area. Must be positive.")
    return pi * a * b

def rhombus_area(d1, d2):
    #Calculate the area of a rhombus given its diagonals.
    if not (isinstance(d1, (float, int)) and isinstance(d2, (float, int))):
        raise ValueError("Invalid rhombus area. Must be numbers.")
    if d1 < 0 or d2 < 0:
        raise ValueError("Invalid rhombus area. Must be positive.")
    return 0.5 * d1 * d2