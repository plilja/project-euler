from unittest import TestCase

from sum_square_difference import *


class TestSumSquareDifference(TestCase):
    def test_sum_square_difference_up_to_1_is_0(self):
        self.assertEqual(sum_square_difference(1), 0)

    def test_sum_square_difference_up_to_2_is_1(self):
        self.assertEqual(sum_square_difference(2), 4)

    def test_sum_square_difference_up_to_3_is_22(self):
        self.assertEqual(sum_square_difference(3), 22)

    def test_sum_square_difference_up_to_4_is_22(self):
        self.assertEqual(sum_square_difference(4), 70)

    def test_sum_square_difference_up_to_100_is_22(self):
        self.assertEqual(sum_square_difference(100), 25164150)

