from unittest import TestCase

from large_prime_factor import *


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

    def test_project_euler_input(self):
        self.assertEqual(largest_prime_factor(600851475143), 6857)