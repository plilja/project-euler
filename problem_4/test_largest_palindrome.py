from unittest import TestCase

from largest_palindrome import *


class TestLargestPalindrome(TestCase):
    def test_largest_palindrome_product_of_two_one_digit_numbers_is_9(self):
        self.assertEqual(largest_palindrome(1), 9)

    def test_largest_palindrome_product_of_two_two_digit_numbers_is_9009(self):
        self.assertEqual(largest_palindrome(2), 9009)

    def test_largest_palindrome_product_of_two_three_digit_numbers_is_906609(self):
        self.assertEqual(largest_palindrome(3), 906609)