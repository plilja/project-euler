import unittest

from number_spiral_diagonals import *


class TestNumberSpiralDiagonals(unittest.TestCase):
    def test_number_spiral_diagonals(self):
        self.assertEqual(number_spiral_diagonals(1), 1)
        self.assertEqual(number_spiral_diagonals(3), 25)
        self.assertEqual(number_spiral_diagonals(5), 101)
        self.assertEqual(number_spiral_diagonals(7), 261)

    def test_illegal_input(self):
        with self.assertRaises(ValueError):
            number_spiral_diagonals(6)
        with self.assertRaises(ValueError):
            number_spiral_diagonals(10)

    def test_project_euler_input(self):
        self.assertEqual(number_spiral_diagonals(1001), 669171001)


if __name__ == '__main__':
    unittest.main()
