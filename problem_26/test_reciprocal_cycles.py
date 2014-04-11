import unittest

from reciprocal_cycles import *


class TestReciprocalCycles(unittest.TestCase):
    def test_reciprocal_cycles(self):
        self.assertEqual(reciprocal_cycles(1), 1)
        self.assertEqual(reciprocal_cycles(2), 1)
        self.assertEqual(reciprocal_cycles(3), 3)
        self.assertEqual(reciprocal_cycles(4), 3)
        self.assertEqual(reciprocal_cycles(6), 3)
        self.assertEqual(reciprocal_cycles(7), 7)
        self.assertEqual(reciprocal_cycles(8), 7)
        self.assertEqual(reciprocal_cycles(9), 7)
        self.assertEqual(reciprocal_cycles(10), 7)
        self.assertEqual(reciprocal_cycles(14), 7)
        self.assertEqual(reciprocal_cycles(17), 17)

    def test_project_euler_input(self):
        self.assertEqual(reciprocal_cycles(999), 983)


if __name__ == '__main__':
    unittest.main()
