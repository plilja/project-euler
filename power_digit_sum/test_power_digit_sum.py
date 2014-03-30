import unittest

from power_digit_sum import *


class TestPowerDigitSum(unittest.TestCase):
    def test_power_digit_sum(self):
        self.assertEqual(power_digit_sum(0), 1)
        self.assertEqual(power_digit_sum(1), 2)
        self.assertEqual(power_digit_sum(2), 4)
        self.assertEqual(power_digit_sum(4), 7)
        self.assertEqual(power_digit_sum(15), 26)

    def test_project_euler_input(self):
        self.assertEqual(power_digit_sum(1000), 1366)


if __name__ == '__main__':
    unittest.main()
