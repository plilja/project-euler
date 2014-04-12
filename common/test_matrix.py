import unittest

from matrix import Matrix


class TestMatrix(unittest.TestCase):
    def test_illegal_row_idx(self):
        matrix = Matrix(10, 10)
        with self.assertRaises(ValueError):
            matrix[10]
        with self.assertRaises(ValueError):
            matrix[-1]

    def test_illegal_column_idx(self):
        matrix = Matrix(10, 10)
        with self.assertRaises(ValueError):
            matrix[0][10]
        with self.assertRaises(ValueError):
            matrix[0][-1]

    def test_set_and_get_item(self):
        matrix = Matrix(2, 2)
        matrix[1][1] = 3
        self.assertEqual(matrix[1][1], 3)

    def test_get_unset_item_should_return_0(self):
        matrix = Matrix(2, 2)
        self.assertEqual(matrix[1][1], 0)

    def test_iter_over_one_row(self):
        m = Matrix(3, 3)
        m[1][0] = 1
        m[1][1] = 2
        m[1][2] = 3
        self.assertEqual([x for x in m.row(1)], [1, 2, 3])
        self.assertEqual([x for x in m[1]], [1, 2, 3])

    def test_iter_over_one_column(self):
        m = Matrix(3, 3)
        m[0][1] = 1
        m[1][1] = 2
        m[2][1] = 3
        self.assertEqual([x for x in m.column(1)], [1, 2, 3])

    def test_slice_row(self):
        m = Matrix(3, 7)
        m[1][0] = 1
        m[1][1] = 0
        m[1][2] = 2
        m[1][3] = 0
        m[1][4] = 3
        m[1][5] = 0
        m[1][6] = 4
        self.assertEqual([x for x in m[1][0:7:2]], [1, 2, 3, 4])
        self.assertEqual([x for x in m[1][0:7]], [1, 0, 2, 0, 3, 0, 4])

    def test_transpose_single_cell_matrix(self):
        m = Matrix(1, 1)
        m[0][0] = 3
        mt = m.transpose()
        self.assertEqual(mt[0][0], 3)

    def test_transpose_2_by_2_matrix(self):
        m = Matrix(2, 2)
        m[0][0] = 1
        m[0][1] = 2
        m[1][0] = 3
        m[1][1] = 4
        mt = m.transpose()
        self.assertEqual(mt[0][0], 1)
        self.assertEqual(mt[0][1], 3)
        self.assertEqual(mt[1][0], 2)
        self.assertEqual(mt[1][1], 4)

    def test_transpose_non_quadratic_matrix(self):
        m = Matrix(2, 3)
        m[0][0] = 1
        m[0][1] = 2
        m[0][2] = 3
        m[1][0] = 4
        m[1][1] = 5
        m[1][2] = 6
        mt = m.transpose()
        self.assertEqual(mt[0][0], 1)
        self.assertEqual(mt[1][0], 2)
        self.assertEqual(mt[2][0], 3)
        self.assertEqual(mt[0][1], 4)
        self.assertEqual(mt[1][1], 5)
        self.assertEqual(mt[2][1], 6)


if __name__ == '__main__':
    unittest.main()
