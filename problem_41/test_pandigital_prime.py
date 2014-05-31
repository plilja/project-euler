import unittest

from pandigital_prime import *


class PandigitalPrimeTest(unittest.TestCase):
    def test_pandigital_primes(self):
        self.assertEqual(largest_pandigital_primes(4), 4231)
        self.assertEqual(largest_pandigital_primes(5), 4231)
        self.assertEqual(largest_pandigital_primes(6), 4231)
        self.assertEqual(largest_pandigital_primes(7), 7652413)

    def test_project_euler(self):
        self.assertEqual(largest_pandigital_primes(9), 7652413)


if __name__ == '__main__':
    unittest.main()
