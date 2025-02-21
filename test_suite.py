import unittest
import time

# Import the TestShapes class
from test.test_Lab3_Nolan_Princess import TestShapes

def run_tests(choice):
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()

    if choice == 'c':
        suite.addTests(loader.loadTestsFromName('test.test_Lab3_Nolan_Princess.TestShapes.test_circle_area_valid'))
        suite.addTests(loader.loadTestsFromName('test.test_Lab3_Nolan_Princess.TestShapes.test_circle_area_invalid'))
    elif choice == 't':
        suite.addTests(loader.loadTestsFromName('test.test_Lab3_Nolan_Princess.TestShapes.test_trapezium_area_valid'))
        suite.addTests(loader.loadTestsFromName('test.test_Lab3_Nolan_Princess.TestShapes.test_trapezium_area_invalid'))
    elif choice == 'e':
        suite.addTests(loader.loadTestsFromName('test.test_Lab3_Nolan_Princess.TestShapes.test_ellipse_area_valid'))
        suite.addTests(loader.loadTestsFromName('test.test_Lab3_Nolan_Princess.TestShapes.test_ellipse_area_invalid'))
    elif choice == 'r':
        suite.addTests(loader.loadTestsFromName('test.test_Lab3_Nolan_Princess.TestShapes.test_rhombus_area_valid'))
        suite.addTests(loader.loadTestsFromName('test.test_Lab3_Nolan_Princess.TestShapes.test_rhombus_area_invalid'))
    else:
        print("Invalid choice. Please try again.")
        return

    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    while True:
        time.sleep(0.1)
        print("\nEnter a shape to test ('c' for Circle, 't' for Trapezium, 'e' for Ellipse, 'r' for Rhombus, 'q' to quit):")
        choice = input("Your choice: ")
        if choice == 'q':
            break
        run_tests(choice)