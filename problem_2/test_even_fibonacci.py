from unittest import TestCase

from even_fibonacci import *


class TestEvenFibonacciSum(TestCase):
    def test_no_numbers(self):
        self.assertEqual(even_fibonacci(1), 0)

    def test_one_even_number(self):
        self.assertEqual(even_fibonacci(2), 2)

    def test_one_even_one_odd_number(self):
        self.assertEqual(even_fibonacci(3), 2)

    def test_two_even_numbers(self):
        self.assertEqual(even_fibonacci(8), 10)

    def test_numbers_smaller_than_4_million(self):
        self.assertEqual(even_fibonacci(3999999), 4613732)

    def test_numbers_smaller_than_400_billion_and_one(self):
        self.assertEqual(even_fibonacci(400000000001), 478361013020)


class TestFibonacciNumbers(TestCase):
    def test_no_numbers(self):
        self.assertEqual(fibonacci_numbers_up_to(0), [])

    def test_two_number(self):
        self.assertEqual(fibonacci_numbers_up_to(1), [1, 1])

    def test_three_numbers(self):
        self.assertEqual(fibonacci_numbers_up_to(2), [1, 1, 2])

    def test_four_numbers(self):
        self.assertEqual(fibonacci_numbers_up_to(3), [1, 1, 2, 3])

    def test_up_to_10(self):
        self.assertEqual(fibonacci_numbers_up_to(10), [1, 1, 2, 3, 5, 8])

