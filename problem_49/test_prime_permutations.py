import unittest

from prime_permutations import *


class PrimePermutationsTest(unittest.TestCase):
    def test_prime_permutations(self):
        self.assertEqual(sorted(prime_permutations()), sorted([2969, 6299, 9629]))


if __name__ == '__main__':
    unittest.main()
