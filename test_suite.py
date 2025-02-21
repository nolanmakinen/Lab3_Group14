import unittest
from test.Lab3_Nolan_Princess import TestShapes


def run_tests(choice):
    loader = unittest.TestLoader()

    if choice == 'c':
        suite = loader.loadTestsFromTestCase(TestShapes)
        tests = [t for t in suite if 'circle_area' in t.id()]
    elif choice == 't':
        suite = loader.loadTestsFromTestCase(TestShapes)
        tests = [t for t in suite if 'trapezium_area' in t.id()]
    elif choice == 'e':
        suite = loader.loadTestsFromTestCase(TestShapes)
        tests = [t for t in suite if 'ellipse_area' in t.id()]
    elif choice == 'r':
        suite = loader.loadTestsFromTestCase(TestShapes)
        tests = [t for t in suite if 'rhombus_area' in t.id()]
    else:
        print("Invalid choice. Exiting.")
        return

    if tests:
        shape_suite = unittest.TestSuite(tests)
        runner = unittest.TextTestRunner()
        runner.run(shape_suite)
    else:
        print(f"No tests found for choice '{choice}'.")


if __name__ == "__main__":
    print("Enter a shape to test ('c' for Circle, 't' for Trapezium, 'e' for Ellipse, 'r' for Rhombus):")
    choice = input().strip().lower()
    run_tests(choice)