import unittest

from integer_right_triangles import *


class IntegerRightTrianglesTest(unittest.TestCase):
    def test_integer_right_triangles(self):
        self.assertEqual(integer_right_triangles(1), set())
        self.assertEqual(integer_right_triangles(2), set())
        self.assertEqual(integer_right_triangles(3), set())
        self.assertEqual(integer_right_triangles(120), {(30, 40, 50), (24, 45, 51), (20, 48, 52)})

    def test_project_euler(self):
        len_with_most_solutions = (1, -1)
        for i in range(1, 1001):
            solutions_for_i = integer_right_triangles(i)
            if len(solutions_for_i) > len_with_most_solutions[1]:
                len_with_most_solutions = (i, len(solutions_for_i))

        self.assertEqual(len_with_most_solutions[0], 840)


if __name__ == '__main__':
    unittest.main()
