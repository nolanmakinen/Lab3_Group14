import unittest
from app.Lab3_Nolan_Princess import circle_area, trapezium_area, ellipse_area, rhombus_area


class TestShapes(unittest.TestCase):

    def setUp(self):
        print("Setup: Preparing tests...")

    def tearDown(self):
        print("Teardown: Cleaning up after tests...")

    def test_circle_area_valid(self):
        self.assertAlmostEqual(circle_area(3), 28.274333882308138)

    def test_circle_area_invalid(self):
        with self.assertRaises(ValueError):
            circle_area(-1)

    # Trapezium Area Tests


def test_trapezium_area_valid(self):
    self.assertAlmostEqual(trapezium_area(3, 4, 5), 17.5)


def test_trapezium_area_invalid(self):
    with self.assertRaises(ValueError):
        trapezium_area(-3, 4, 5)

    # Ellipse Area Tests


def test_ellipse_area_valid(self):
    self.assertAlmostEqual(ellipse_area(3, 5), 47.12388980384689)


def test_ellipse_area_invalid(self):
    with self.assertRaises(ValueError):
        ellipse_area(-3, 5)

    # Rhombus Area Tests


def test_rhombus_area_valid(self):
    self.assertAlmostEqual(rhombus_area(4, 6), 12.0)


def test_rhombus_area_invalid(self):
    with self.assertRaises(ValueError):
        rhombus_area(-4, 6)

if __name__ == "__main__":
    unittest.main()