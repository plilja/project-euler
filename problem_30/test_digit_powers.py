import unittest

from digit_powers import *


class TestDigitPowers(unittest.TestCase):
    def test_digit_first_power(self):
        self.assertEqual(sum_digit_powers(1), [])

    def test_digit_second_powers(self):
        self.assertEqual(sum_digit_powers(2), [])

    def test_digit_third_powers(self):
        self.assertEqual(sum_digit_powers(3), [153, 370, 371, 407])

    def test_digit_fourth_powers(self):
        self.assertEqual(sum_digit_powers(4), [1634, 8208, 9474])

    def test_project_euler_input(self):
        self.assertEqual(sum(sum_digit_powers(5)), 443839)


if __name__ == '__main__':
    unittest.main()
