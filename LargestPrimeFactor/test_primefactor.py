from unittest import TestCase

from primefactor import *


class TestLargestPrimeFactor(TestCase):
    def test_largest_prime_factor_of_1_is_1(self):
        self.assertEqual(largest_prime_factor(1), 1)

    def test_largest_prime_factor_of_2_is_2(self):
        self.assertEqual(largest_prime_factor(2), 2)

    def test_largest_prime_factor_of_3_is_3(self):
        self.assertEqual(largest_prime_factor(3), 3)

    def test_largest_prime_factor_of_4_is_2(self):
        self.assertEqual(largest_prime_factor(4), 2)

    def test_largest_prime_factor_of_13195_is_29(self):
        self.assertEqual(largest_prime_factor(13195), 29)

    def test_largest_prime_factor_of_600851475143_is_6857(self):
        self.assertEqual(largest_prime_factor(600851475143), 6857)


class TestPrimeFactors(TestCase):
    def test_prime_factors_of_1_is_1(self):
        self.assertEqual(prime_factors(1), [1])

    def test_prime_factors_of_prime_number_is_the_prime_number(self):
        self.assertEqual(prime_factors(2), [2])
        self.assertEqual(prime_factors(7), [7])
        self.assertEqual(prime_factors(17), [17])

    def test_prime_factors_of_4_is_2_and_2(self):
        self.assertEqual(prime_factors(4), [2, 2])

    def test_prime_factors_of_10_is_2_and_5(self):
        self.assertEqual(sorted(prime_factors(10)), [2, 5])

    def test_prime_factors_of_300_is_2_3_and_5(self):
        self.assertEqual(sorted(prime_factors(30)), [2, 3, 5])