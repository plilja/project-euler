import unittest

from fibonacci_with_digits import *


class TestFibonacciWithDigits(unittest.TestCase):
    def test_fibonacci_with_digits(self):
        self.assertEqual(fibonacci_with_digits(1), 1)
        self.assertEqual(fibonacci_with_digits(2), 7)
        self.assertEqual(fibonacci_with_digits(3), 12)
        self.assertEqual(fibonacci_with_digits(4), 17)
        self.assertEqual(fibonacci_with_digits(5), 21)
        self.assertEqual(fibonacci_with_digits(6), 26)

    def test_project_euler_input(self):
        self.assertEqual(fibonacci_with_digits(1000), 4782)


if __name__ == '__main__':
    unittest.main()
