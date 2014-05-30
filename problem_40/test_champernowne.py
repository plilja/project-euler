import unittest
import operator

from champernowne import *


class ChampernowneTest(unittest.TestCase):
    def test_champernownes_constant(self):
        self.assertEqual(champernownes_nth_decimal(12), 1)
        self.assertEqual(champernownes_nth_decimal(1), 1)
        self.assertEqual(champernownes_nth_decimal(2), 2)
        self.assertEqual(champernownes_nth_decimal(14), 1)
        self.assertEqual(champernownes_nth_decimal(15), 2)
        self.assertEqual(champernownes_nth_decimal(17), 3)
        self.assertEqual(champernownes_nth_decimal(32), 2)

    def test_project_euler(self):
        res = reduce(operator.mul, map(champernownes_nth_decimal, [1, 10, 100, 1000, 10000, 100000, 1000000]))
        self.assertEqual(res, 210)

    if __name__ == '__main__':
        unittest.main()
