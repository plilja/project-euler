import unittest

from powers import *


class PowersTest(unittest.TestCase):
    def test_powers(self):
        self.assertEqual(powers(1, 1), 1)
        self.assertEqual(powers(1, 2), 1)
        self.assertEqual(powers(1, 3), 1)
        self.assertEqual(powers(2, 1), 2)
        self.assertEqual(powers(3, 1), 3)
        self.assertEqual(powers(2, 2), 4)
        self.assertEqual(powers(3, 2), 9)
        self.assertEqual(powers(3, 4), 9)
        self.assertEqual(powers(3, 5), 9)
        self.assertEqual(powers(3, 6), 18)
        self.assertEqual(powers(10, 1), 9)
        self.assertEqual(powers(10, 2), 13)
        self.assertEqual(powers(4, 5), 13)

    def test_project_euler(self):
        self.assertEqual(powers(100, 100), 972)


if __name__ == '__main__':
    unittest.main()
