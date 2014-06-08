import unittest

from distinct_consecutive_prime_factors import *


class DistinctConsecutivePrimeFactorsTest(unittest.TestCase):
    def test_distinct_prime_factors(self):
        self.assertEqual(distinct_consecutive_prime_factors(0, 0), [])
        self.assertEqual(distinct_consecutive_prime_factors(1, 1), [2])
        self.assertEqual(distinct_consecutive_prime_factors(1, 2), [2, 3])
        self.assertEqual(distinct_consecutive_prime_factors(2, 2), [14, 15])
        self.assertEqual(distinct_consecutive_prime_factors(3, 3), [644, 645, 646])

    def test_project_euler(self):
        self.assertEqual(distinct_consecutive_prime_factors(4, 4), [134043, 134044, 134045, 134046])


if __name__ == '__main__':
    unittest.main()
