import unittest

from quadratic_primes import *


class TestQuadraticPrimes(unittest.TestCase):
    def test_quadratic_primes(self):
        self.assertEqual(quadratic_primes(3), (-1, 2))
        self.assertEqual(quadratic_primes(5), (-2, 3))
        self.assertEqual(quadratic_primes(10), (-3, 7))
        self.assertEqual(quadratic_primes(42), (-1, 41))
        self.assertEqual(quadratic_primes(100), (-15, 97))
        self.assertEqual(quadratic_primes(200), (-25, 197))
        self.assertEqual(quadratic_primes(300), (-31, 281))

    def test_project_euler_input(self):
        result = quadratic_primes(1000)
        self.assertEqual(result, (-61, 971))
        self.assertEqual(result[0] * result[1], -59231)


if __name__ == '__main__':
    unittest.main()
