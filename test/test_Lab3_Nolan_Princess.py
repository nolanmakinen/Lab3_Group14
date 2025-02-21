import unittest
from app.Lab3_Nolan_Princess import circle_area, trapezium_area, ellipse_area, rhombus_area

class TestShapes(unittest.TestCase):

    def setUp(self):
        print("Setup: Preparing tests...")  # Fixture: Runs before every test

    def tearDown(self):
        print("Teardown: Cleaning up after tests...")  # Fixture: Runs after every test

    # Uncommented Circle Tests
    def test_circle_area_valid(self):

    def test_circle_area_invalid(self):

    # Trapezium Tests
    def test_trapezium_area_valid(self):

    def test_trapezium_area_invalid(self):

    # Ellipse Tests
    def test_ellipse_area_valid(self):
        # Standard case
        self.assertAlmostEqual(ellipse_area(10, 5), 157.07963267948946, places=5)

        # Edge case where a == b, behaves like a circle
        self.assertAlmostEqual(ellipse_area(10, 10), 314.1592653589793, places=5)

        # Edge case with a or b = 0, area should be 0
        self.assertEqual(ellipse_area(0, 10), 0)
        self.assertEqual(ellipse_area(10, 0), 0)

    # Test invalid ellipse area cases
    def test_ellipse_area_invalid(self):
        # Negative values should raise an error
        with self.assertRaises(ValueError):
            ellipse_area(-10, 5)
        with self.assertRaises(ValueError):
            ellipse_area(10, -5)

        # Non-numeric inputs should raise a TypeError
        with self.assertRaises(TypeError):
            ellipse_area("a", 120)
        with self.assertRaises(TypeError):
            ellipse_area(10, "b")

    # Rhombus Tests
    def test_rhombus_area_valid(self):

    def test_rhombus_area_invalid(self):

if __name__ == "__main__":
    unittest.main()
