import unittest
from math import *

from digit_powers import *
from common.functions import number_as_digits


class DigitPowersTest(unittest.TestCase):
    def test_digit_powers(self):
        for num in digit_powers():
            digits = number_as_digits(num)
            root = int(round(pow(num, 1.0 / len(digits))))
            self.assertEqual(num, root ** len(digits))

    def test_sample_input(self):
        res = set(digit_powers())
        self.assertTrue(16807 in res)
        self.assertTrue(134217728 in res)

    def test_answer(self):
        self.assertEqual(49, len(digit_powers()))


if __name__ == '__main__':
    unittest.main()
