import unittest

from amicable_numbers import *


class TestAmicableNumbers(unittest.TestCase):
    def test_1_is_not_an_amicable_number(self):
        self.assertFalse(1 in amicable_numbers_less_than(2))

    def test_when_sum_of_divisors_of_a_number_equals_the_number_itself_then_the_number_is_not_an_amicable_number(self):
        self.assertFalse(6 in amicable_numbers_less_than(7))
        self.assertFalse(28 in amicable_numbers_less_than(7))

    def test_the_first_amicable_number_is_220(self):
        self.assertEqual(amicable_numbers_less_than(221), [220])

    def test_the_second_amicable_number_is_284(self):
        self.assertEqual(amicable_numbers_less_than(285), [220, 284])

    def test_project_euler_input(self):
        self.assertEqual(sum(amicable_numbers_less_than(10000)), 31626)


if __name__ == '__main__':
    unittest.main()



