import unittest

from cnr import *


class CnrTest(unittest.TestCase):
    def test_no_solutions(self):
        self.assertEqual(cnr_larger_than(1, 2), 0)
        self.assertEqual(cnr_larger_than(3, 4), 0)

    def test_one_solution(self):
        self.assertEqual(cnr_larger_than(2, 2), 1)

    def test_two_solutions(self):
        self.assertEqual(cnr_larger_than(3, 3), 2)

    def test_project_euler(self):
        self.assertEqual(cnr_larger_than(100, 1000000), 4075)


if __name__ == '__main__':
    unittest.main()
