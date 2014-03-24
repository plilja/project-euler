from unittest import *

from smallest_multiple import *


class TestSmallestMultiple(TestCase):
    def test_smallest_multiple_that_is_divisible_by_1_is_1(self):
        self.assertEqual(smallest_multiple([1]), 1)

    def test_smallest_multiple_that_is_divisible_by_1_and_2_is_2(self):
        self.assertEqual(smallest_multiple([1, 2]), 2)

    def test_smallest_multiple_that_is_divisible_by_1_through_3_is_6(self):
        self.assertEqual(smallest_multiple([1, 2]), 2)

    def test_smallest_multiple_that_is_divisible_by_1_through_6_is_60(self):
        self.assertEqual(smallest_multiple(range(1, 7)), 60)

    def test_smallest_multiple_that_is_divisible_by_4_6_and_8_is_24(self):
        self.assertEqual(smallest_multiple([4, 6, 8]), 24)

    def test_smallest_multiple_that_is_divisible_by_3_4_6_and_8_is_60(self):
        self.assertEqual(smallest_multiple([3, 4, 6, 8]), 24)

    def test_smallest_multiple_that_is_divisible_by_1_through_10_is_2520(self):
        self.assertEqual(smallest_multiple(range(1, 11)), 2520)

    def test_smallest_multiple_that_is_divisible_by_1_through_20_is_232792560(self):
        self.assertEqual(smallest_multiple(range(1, 21)), 232792560)
