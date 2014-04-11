import unittest

from common.primes import PrimeSieve


class Test10001StPrime(unittest.TestCase):
    def test_10001_th_prime_number_is_104743(self):
        prime_sieve = PrimeSieve(500000)
        self.assertEqual(prime_sieve.primes()[10000], 104743)


if __name__ == '__main__':
    unittest.main()
