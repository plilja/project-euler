import unittest

from tri_pen_and_hex import *


class TriPenAndHexTest(unittest.TestCase):
    def test_next_tri_pen_and_hex(self):
        self.assertEqual(next_tri_pen_and_hex(1), 40755)

    def test_project_euler(self):
        self.assertEqual(next_tri_pen_and_hex(40755), 1533776805)


if __name__ == '__main__':
    unittest.main()
