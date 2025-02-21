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

    def test_ellipse_area_invalid(self):

    # Rhombus Tests
    def test_rhombus_area_valid(self):

    def test_rhombus_area_invalid(self):

if __name__ == "__main__":
    unittest.main()
