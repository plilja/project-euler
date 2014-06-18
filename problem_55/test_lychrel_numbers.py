import unittest

from lychrel_numbers import *


class LychrelNumbersTest(unittest.TestCase):
    def test_lychrel_numbers_one_iteration(self):
        self.assertEqual(lychrel_numbers_below(2, 1), [])
        self.assertEqual(lychrel_numbers_below(5, 1), [])
        self.assertEqual(lychrel_numbers_below(10, 1), [5, 6, 7, 8, 9])
        self.assertEqual(lychrel_numbers_below(11, 1), [5, 6, 7, 8, 9])

    def test_196_is_the_first_lychrel_number(self):
        self.assertEqual(lychrel_numbers_below(197, 50), [196])

    def test_project_euler(self):
        self.assertEqual(len(lychrel_numbers_below(10000, 50)), 249)


if __name__ == '__main__':
    unittest.main()
