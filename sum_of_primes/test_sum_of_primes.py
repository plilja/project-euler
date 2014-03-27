import unittest

from prime_sieve.prime_sieve import PrimeSieve


class TestSumOfPrimes(unittest.TestCase):
    def test_sum_of_primes_less_than_two_million(self):
        prime_sieve = PrimeSieve(2000000)
        self.assertEqual(sum(prime_sieve.primes()), 142913828922)


if __name__ == '__main__':
    unittest.main()
