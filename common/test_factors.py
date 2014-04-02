import unittest

from factors import *


class TestPrimeFactors(unittest.TestCase):
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


class TestPrimeFactorization(unittest.TestCase):
    def test_prime_factorization(self):
        self.assertEqual(prime_factorization(1), {1: 1})
        self.assertEqual(prime_factorization(2), {2: 1})
        self.assertEqual(prime_factorization(3), {3: 1})
        self.assertEqual(prime_factorization(4), {2: 2})
        self.assertEqual(prime_factorization(5), {5: 1})
        self.assertEqual(prime_factorization(6), {2: 1, 3: 1})
        self.assertEqual(prime_factorization(8), {2: 3})
        self.assertEqual(prime_factorization(24), {2: 3, 3: 1})


class TestAllFactors(unittest.TestCase):
    def test_all_factors(self):
        self.assertEqual(all_factors(1), {1})
        self.assertEqual(all_factors(2), {1, 2})
        self.assertEqual(all_factors(3), {1, 3})
        self.assertEqual(all_factors(4), {1, 2, 4})
        self.assertEqual(all_factors(6), {1, 2, 3, 6})
        self.assertEqual(all_factors(8), {1, 2, 4, 8})
        self.assertEqual(all_factors(24), {1, 2, 3, 4, 6, 8, 12, 24})

    def test_all_factors_big_number(self):
        self.assertEqual(len(all_factors(76576500)), 576)
        self.assertEqual(len(all_factors(76576500000)), 2016)


if __name__ == '__main__':
    unittest.main()
