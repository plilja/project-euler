import unittest

from lattice_paths import *


class TestLatticePaths(unittest.TestCase):
    def test_0_by_0_grid(self):
        self.assertEqual(lattice_paths(0, 0), 1)

    def test_1_by_1_grid(self):
        self.assertEqual(lattice_paths(1, 1), 2)

    def test_2_by_2_grid(self):
        self.assertEqual(lattice_paths(2, 2), 6)

    def test_3_by_3_grid(self):
        self.assertEqual(lattice_paths(3, 3), 20)

    def test_project_euler_input(self):
        self.assertEqual(lattice_paths(20, 20), 137846528820)


if __name__ == '__main__':
    unittest.main()

