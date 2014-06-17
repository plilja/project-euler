import unittest

from multiple_with_digits import *


class SmallestDoubleTest(unittest.TestCase):
    def test_multiple_of_two(self):
        self.assertEqual(multiple_with_same_digits([2]), 125874)

    def test_multiple_of_three(self):
        self.assertEqual(multiple_with_same_digits([3]), 1035)

    def test_multiple_of_four(self):
        self.assertEqual(multiple_with_same_digits([4]), 1782)

    def test_multiple_of_two_and_three(self):
        self.assertEqual(multiple_with_same_digits([2, 3]), 142857)

    def test_project_euler(self):
        self.assertEqual(multiple_with_same_digits([2, 3, 4, 5, 6]), 142857)


if __name__ == '__main__':
    unittest.main()
