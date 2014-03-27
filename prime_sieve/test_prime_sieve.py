from unittest import TestCase

from prime_sieve import *


prime_numbers_less_than_100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83,
                               89, 97]


class TestPrimeSieve(TestCase):
    def test_prime_sieve_of_size_1_valid_input(self):
        prime_sieve = PrimeSieve(1)
        self.assertFalse(prime_sieve.is_prime(0))
        self.assertFalse(prime_sieve.is_prime(1))

    def test_prime_sieve_of_size_1_invalid_input(self):
        prime_sieve = PrimeSieve(1)
        with self.assertRaises(ValueError):
            prime_sieve.is_prime(2)

    def test_prime_sieve_of_size_2_valid_input(self):
        prime_sieve = PrimeSieve(2)
        self.assertFalse(prime_sieve.is_prime(1))
        self.assertTrue(prime_sieve.is_prime(2))

    def test_prime_sieve_of_size_2_invalid_input(self):
        prime_sieve = PrimeSieve(2)
        with self.assertRaises(ValueError):
            prime_sieve.is_prime(3)

    def test_prime_sieve_of_size_3_invalid_input(self):
        prime_sieve = PrimeSieve(3)
        with self.assertRaises(ValueError):
            prime_sieve.is_prime(4)

    def test_prime_sieve_of_size_3_valid_input(self):
        prime_sieve = PrimeSieve(3)
        self.assertFalse(prime_sieve.is_prime(1))
        self.assertTrue(prime_sieve.is_prime(2))
        self.assertTrue(prime_sieve.is_prime(3))

    def test_prime_sieve_of_size_4_valid_input(self):
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

    def test_10001_th_prime_number_is_104759(self):
        prime_sieve = PrimeSieve(500000)
        self.assertEqual(prime_sieve.primes()[10001], 104759)

