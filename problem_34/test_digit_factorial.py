import unittest

from digit_factorial import *


class TestDigitFactorial(unittest.TestCase):
    def test_digit_factorial(self):
        self.assertEqual([145, 40585], digit_factorial())

    def test_project_euler(self):
        self.assertEqual(sum(digit_factorial()), 40730)


if __name__ == '__main__':
    unittest.main()
