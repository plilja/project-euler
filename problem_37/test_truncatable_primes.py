import unittest

from truncatable_primes import *


class TestTruncatablePrimes(unittest.TestCase):
    def test_truncatable_primes(self):
        _truncatable_primes = truncatable_primes()
        self.assertTrue(23 in _truncatable_primes)
        self.assertTrue(37 in _truncatable_primes)
        self.assertTrue(53 in _truncatable_primes)
        self.assertTrue(73 in _truncatable_primes)
        self.assertTrue(3797 in _truncatable_primes)
        self.assertTrue(len(_truncatable_primes), 11)

    def test_project_euler(self):
        self.assertEqual(sum(truncatable_primes()), 748317)


if __name__ == '__main__':
    unittest.main()
