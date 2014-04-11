import unittest

from non_abundant_sums import *


class TestNonAbundantSums(unittest.TestCase):
    def test_non_abundant_sum(self):
        self.assertEqual(not_sum_of_two_non_abundant(1), [])
        self.assertEqual(not_sum_of_two_non_abundant(2), [1])
        self.assertEqual(not_sum_of_two_non_abundant(3), [1, 2])
        self.assertEqual(not_sum_of_two_non_abundant(4), [1, 2, 3])
        self.assertEqual(not_sum_of_two_non_abundant(13), [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
        self.assertEqual(not_sum_of_two_non_abundant(25), range(1, 24))
        self.assertEqual(not_sum_of_two_non_abundant(31), range(1, 24) + [25, 26, 27, 28, 29])
        self.assertEqual(not_sum_of_two_non_abundant(37), range(1, 24) + [25, 26, 27, 28, 29, 31, 33, 34, 35])
        self.assertTrue(102 not in not_sum_of_two_non_abundant(200))
        self.assertTrue(110 not in not_sum_of_two_non_abundant(200))


    def test_project_euler_input(self):
        self.assertEqual(sum(not_sum_of_two_non_abundant(28124)), 4179871)


if __name__ == '__main__':
    unittest.main()
