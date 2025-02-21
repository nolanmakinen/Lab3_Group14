# Lab3_Group14
Group members: Nolan Makinen & Princess Okerulu
## Purpose of Lab 3
The purpose of Lab 3 was to make a python program that finds the area of circle, trapezium, ellipse, and rhombus. As well as test cases for each shape function
## How the work was divided
| contributor | Parts Created |
|-------------|---------------|
| Nolan Makinen | ellipse & rhombus validation and unit testing |
| Princess Okerulu | circle & trapezium validation and unit testing |
## Provided code
We were provided the following 3 files as a base for this Lab.

Lab3.py
```python 
from math import pi

def circle_area(r):
    if isinstance(r, (int, float)) and r >= 0:
        return pi * (r ** 2)
    else:
        raise ValueError("Invalid radius. Must be a non-negative number.")

def trapezium_area(a, b, h):
    return 0.5 * (a + b) * h
    

def ellipse_area(a, b):
    return pi * a * b
  

def rhombus_area(d1, d2):
    return 0.5 * d1 * d2
```

test_Lab3.py
```python
import unittest
from app.Lab3_firstname1_firstname2 import circle_area, trapezium_area, ellipse_area, rhombus_area

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

   //def test_trapezium_area_valid(self):
        

    //def test_trapezium_area_invalid(self):
       

    //def test_ellipse_area_valid(self):
        

    //def test_ellipse_area_invalid(self):
      

    //def test_rhombus_area_valid(self):
     
    //def test_rhombus_area_invalid(self):
        
if __name__ == "__main__":
    unittest.main()
```

test_suite.py
```python
import unittest

# Import the TestShapes class
from test_Lab3_firstname1_firstname2 import TestShapes

def run_tests(choice):
    suite = unittest.TestSuite()

    if choice == 'c':
        suite.addTest(TestShapes('test_circle_area_valid'))
        suite.addTest(TestShapes('test_circle_area_invalid'))
    elif choice == 't':
        suite.addTest(TestShapes('test_trapezium_area_valid'))
    elif choice == 'e':
        suite.addTest(TestShapes('test_ellipse_area_valid'))
    elif choice == 'r':
        suite.addTest(TestShapes('test_rhombus_area_valid'))
    else:
        print("Invalid choice. Exiting.")
        return

    runner = unittest.TextTestRunner()
    runner.run(suite)


if __name__ == "__main__":
    print("Enter a shape to test ('c' for Circle, 't' for Trapezium, 'e' for Ellipse, 'r' for Rhombus):")
    choice = input().strip().lower()
    run_tests(choice)
```

There is more info about the assignment [here](https://github.com/mdalmaruf/SoftwareTesting/blob/main/Lab3.md)