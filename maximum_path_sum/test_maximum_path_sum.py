import unittest

from maximum_path_sum import *


class TestMaximumPathSum(unittest.TestCase):
    def test_single_line_input(self):
        self.assertEqual(maximum_path_sum([[3]]), 3)
        self.assertEqual(maximum_path_sum([[5]]), 5)
        self.assertEqual(maximum_path_sum([[6]]), 6)

    def test_two_line_input(self):
        self.assertEqual(maximum_path_sum([[3],
                                           [0, 0]]), 3)
        self.assertEqual(maximum_path_sum([[3],
                                           [1, 0]]), 4)
        self.assertEqual(maximum_path_sum([[3],
                                           [0, 1]]), 4)
        self.assertEqual(maximum_path_sum([[4],
                                           [5, 6]]), 10)

    def test_three_line_input(self):
        self.assertEqual(maximum_path_sum([[3],
                                           [2, 3],
                                           [2, 3, 3], ]), 9)
        self.assertEqual(maximum_path_sum([[1],
                                           [7, 1],
                                           [1, 1, 5], ]), 9)
        self.assertEqual(maximum_path_sum([[1],
                                           [5, 1],
                                           [1, 1, 7], ]), 9)
        self.assertEqual(maximum_path_sum([[1],
                                           [1, 5],
                                           [1, 7, 5], ]), 13)

    def test_four_line_input(self):
        self.assertEqual(maximum_path_sum([[3],
                                           [7, 4],
                                           [2, 4, 6],
                                           [8, 5, 9, 3], ]), 23)
        self.assertEqual(maximum_path_sum([[3],
                                           [7, 4],
                                           [2, 6, 3],
                                           [8, 9, 6, 3], ]), 25)

    def test_project_euler_input(self):
        self.assertEqual(maximum_path_sum([[75],
                                           [95, 64],
                                           [17, 47, 82],
                                           [18, 35, 87, 10],
                                           [20, 4, 82, 47, 65],
                                           [19, 1, 23, 75, 3, 34],
                                           [88, 02, 77, 73, 7, 63, 67],
                                           [99, 65, 4, 28, 6, 16, 70, 92],
                                           [41, 41, 26, 56, 83, 40, 80, 70, 33],
                                           [41, 48, 72, 33, 47, 32, 37, 16, 94, 29],
                                           [53, 71, 44, 65, 25, 43, 91, 52, 97, 51, 14],
                                           [70, 11, 33, 28, 77, 73, 17, 78, 39, 68, 17, 57],
                                           [91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 48],
                                           [63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31],
                                           [4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23], ]), 1074)


if __name__ == '__main__':
    unittest.main()
