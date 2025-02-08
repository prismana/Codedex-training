import unittest
import math

def get_sqrt(n):
    return math.sqrt(n)

def divide(a, b):
    return a / b

class TestUnexpected(unittest.TestCase):
    def test_sqrt(self):
        self.assertEqual(get_sqrt(144), 12)
    
    def test_sqrt_with_negative_number(self):
        with self.assertRaises(ValueError):
            self.assertIn(-23, -12)

    def test_devide(self):
        self.assertEqual(divide(144, 12), 12)

    def test_divide_with_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.assertIn(4, 0)

if __name__ == '__main__':
    unittest.main()
