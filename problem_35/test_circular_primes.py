import unittest

from circular_primes import *


class TestCircularPrimes(unittest.TestCase):
    def test_circular_primes(self):
        self.assertEqual([], circular_primes(1))
        self.assertEqual([2], circular_primes(2))
        self.assertEqual([2, 3], circular_primes(3))
        self.assertEqual([2, 3], circular_primes(4))
        self.assertEqual([2, 3, 5], circular_primes(5))
        self.assertEqual([2, 3, 5, 7, 11], circular_primes(11))
        self.assertEqual([2, 3, 5, 7, 11, 13, 17, 31, 37], circular_primes(37))
        self.assertEqual([2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, 97], circular_primes(100))

    def test_project_euler_input(self):
        self.assertEqual(len(circular_primes(1000000)), 55)


if __name__ == '__main__':
    unittest.main()
