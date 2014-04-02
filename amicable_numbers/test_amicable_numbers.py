import unittest

from amicable_numbers import *


class TestAmicableNumbers(unittest.TestCase):
    def test_amicable_numbers_less_than(self):
        self.assertEqual(amicable_numbers_less_than(1), [])
        self.assertEqual(amicable_numbers_less_than(2), [1])
        self.assertEqual(amicable_numbers_less_than(3), [1])
        self.assertEqual(amicable_numbers_less_than(6), [1])
        self.assertEqual(amicable_numbers_less_than(7), [1, 6])
        self.assertEqual(amicable_numbers_less_than(29), [1, 6, 28])
        self.assertEqual(amicable_numbers_less_than(29), [1, 6, 28])
        self.assertEqual(amicable_numbers_less_than(221), [1, 6, 28, 220])
        self.assertEqual(amicable_numbers_less_than(285), [1, 6, 28, 220, 284])

    def test_project_euler_input(self):
        self.assertEqual(sum(amicable_numbers_less_than(10001)), 40285)


if __name__ == '__main__':
    unittest.main()



