import unittest

from factorial_digit_sum import *


class TestFactorialDigitSum(unittest.TestCase):
    def test_1(self):
        self.assertEqual(factorial_digit_sum(1), 1)

    def test_2(self):
        self.assertEqual(factorial_digit_sum(2), 2)

    def test_3(self):
        self.assertEqual(factorial_digit_sum(3), 6)

    def test_4(self):
        self.assertEqual(factorial_digit_sum(4), 6)

    def test_10(self):
        self.assertEqual(factorial_digit_sum(10), 27)

    def test_project_euler_input(self):
        self.assertEqual(factorial_digit_sum(100), 648)


if __name__ == '__main__':
    unittest.main()
