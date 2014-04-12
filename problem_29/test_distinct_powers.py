import unittest

from distinct_powers import *


class TestDistinctPowers(unittest.TestCase):
    def test_distinct_powers(self):
        self.assertEqual(distinct_powers(2), 1)
        self.assertEqual(distinct_powers(3), 4)
        self.assertEqual(distinct_powers(4), 8)
        self.assertEqual(distinct_powers(5), 15)

    def test_project_euler_input(self):
        self.assertEqual(distinct_powers(100), 9183)


if __name__ == '__main__':
    unittest.main()
