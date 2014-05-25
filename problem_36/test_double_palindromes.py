import unittest

from double_palindromes import *


class TestDoublePalindromes(unittest.TestCase):
    def test_double_palindromes(self):
        self.assertTrue([1], double_palindromes(2))
        self.assertTrue([1, 3], double_palindromes(4))
        self.assertTrue([1, 3, 5], double_palindromes(6))
        self.assertTrue([1, 3, 5, 7, 9], double_palindromes(10))
        self.assertTrue([1, 3, 5, 7, 9, 33, 99], double_palindromes(100))
        self.assertTrue(585 in double_palindromes(586))


    def test_project_euler(self):
        self.assertEqual(sum(double_palindromes(1000000)), 872187)


if __name__ == '__main__':
    unittest.main()
