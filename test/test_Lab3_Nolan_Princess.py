import unittest
from app.Lab3_Nolan_Princess import circle_area, trapezium_area, ellipse_area, rhombus_area

class TestShapes(unittest.TestCase):

    def setUp(self):
        print("Setup: Preparing tests...")  # Fixture: Runs before every test

    def tearDown(self):
        print("Teardown: Cleaning up after tests...")  # Fixture: Runs after every test

        # Circle Tests
        def test_circle_area_valid(self):
            # Standard case
            self.assertAlmostEqual(circle_area(3), 28.274333882308138, places=5)

            # Edge case with radius = 0 (should be 0)
            self.assertEqual(circle_area(0), 0)

            # Large value
            self.assertAlmostEqual(circle_area(1000), 3141592.653589793, places=5)

        def test_circle_area_invalid(self):
            # Negative values should raise an error
            with self.assertRaises(ValueError):
                circle_area(-3)

            # Non-numeric inputs should raise a TypeError
            with self.assertRaises(TypeError):
                circle_area("a")
            with self.assertRaises(TypeError):
                circle_area(None)

        # Trapezium Tests
        def test_trapezium_area_valid(self):
            # Standard case
            self.assertAlmostEqual(trapezium_area(3, 4, 5), 17.5, places=5)

            # Case where one base or height is zero, area should be 0
            self.assertEqual(trapezium_area(0, 4, 5), 10)
            self.assertEqual(trapezium_area(3, 0, 5), 7.5)
            self.assertEqual(trapezium_area(3, 4, 0), 0)

        def test_trapezium_area_invalid(self):
            # Negative values should raise an error
            with self.assertRaises(ValueError):
                trapezium_area(-3, 4, 5)
            with self.assertRaises(ValueError):
                trapezium_area(3, -4, 5)
            with self.assertRaises(ValueError):
                trapezium_area(3, 4, -5)

            # Non-numeric inputs should raise a TypeError
            with self.assertRaises(TypeError):
                trapezium_area("a", 4, 5)
            with self.assertRaises(TypeError):
                trapezium_area(3, "b", 5)
            with self.assertRaises(TypeError):
                trapezium_area(3, 4, "c")
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
        # Standard case
        self.assertEqual(rhombus_area(10, 5), 25)

        # Case where diagonals are zero, area should be 0
        self.assertEqual(rhombus_area(0, 10), 0)
        self.assertEqual(rhombus_area(10, 0), 0)

        # Case where diagonals are the same (should still work as normal)
        self.assertEqual(rhombus_area(5, 5), 12.5)

    # Test invalid rhombus area cases
    def test_rhombus_area_invalid(self):
        # Negative values should raise an error
        with self.assertRaises(ValueError):
            rhombus_area(-10, 5)
        with self.assertRaises(ValueError):
            rhombus_area(10, -5)

        # Non-numeric inputs should raise a TypeError
        with self.assertRaises(TypeError):
            rhombus_area("a", 120)
        with self.assertRaises(TypeError):
            rhombus_area(10, "b")

if __name__ == "__main__":
    unittest.main()