from unittest import TestCase

from primes import *


prime_numbers_less_than_100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
                               89, 97]


class TestPrimeSieve(TestCase):
    def test_prime_sieve_of_size_1(self):
        prime_sieve = PrimeSieve(1)
        self.assertFalse(prime_sieve.is_prime(0))
        self.assertFalse(prime_sieve.is_prime(1))

    def test_prime_sieve_of_size_3(self):
        prime_sieve = PrimeSieve(3)
        self.assertFalse(prime_sieve.is_prime(1))
        self.assertTrue(prime_sieve.is_prime(2))
        self.assertTrue(prime_sieve.is_prime(3))

    def test_prime_sieve_of_size_4(self):
        prime_sieve = PrimeSieve(4)
        self.assertFalse(prime_sieve.is_prime(1))
        self.assertTrue(prime_sieve.is_prime(2))
        self.assertTrue(prime_sieve.is_prime(3))
        self.assertFalse(prime_sieve.is_prime(4))

    def test_prime_sieve_of_size_100(self):
        prime_sieve = PrimeSieve(100)
        for prime in prime_numbers_less_than_100:
            self.assertTrue(prime_sieve.is_prime(prime))
        for composite in set(range(1, 101)) - set(prime_numbers_less_than_100):
            self.assertFalse(prime_sieve.is_prime(composite))

    def test_list_prime_numbers_sieve_size_1(self):
        prime_sieve = PrimeSieve(1)
        self.assertEqual(prime_sieve.primes(), tuple())

    def test_list_prime_numbers_less_than_100(self):
        prime_sieve = PrimeSieve(100)
        self.assertEqual(prime_sieve.primes(), tuple(prime_numbers_less_than_100))

    def test_prime_sieve_grows_when_needed(self):
        prime_sieve = PrimeSieve(2)
        self.assertTrue(prime_sieve.is_prime(3))
        self.assertEqual(prime_sieve.current_size(), 6)

    def test_prime_sieve_default_size(self):
        prime_sieve = PrimeSieve()
        self.assertTrue(prime_sieve.is_prime(97))
        self.assertTrue(prime_sieve.is_prime(89))

    def test_prime_sieve_with_default_size_grows_if_prime_is_out_range(self):
        prime_sieve = PrimeSieve()
        self.assertTrue(prime_sieve.current_size(), 1000)
        self.assertTrue(prime_sieve.is_prime(1093))
        self.assertFalse(prime_sieve.is_prime(1095))

    def test_primes_less_than_n_when_n_is_less_than_size(self):
        prime_sieve = PrimeSieve(11)
        self.assertEqual(prime_sieve.primes_less_than(10), (2, 3, 5, 7))

    def test_primes_less_than_n_when_n_is_greater_than_than_size(self):
        prime_sieve = PrimeSieve(9)
        self.assertEqual(prime_sieve.primes_less_than(10), (2, 3, 5, 7))
