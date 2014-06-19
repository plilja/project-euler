import unittest

from ulam_spiral import *


class UlamSpiralTest(unittest.TestCase):
    def test_ulam_spiral_corners(self):
        corners = ulam_spiral_corners()
        self.assertEqual(corners.next(), (1, 1, 1, 1))
        self.assertEqual(corners.next(), (3, 5, 7, 9))
        self.assertEqual(corners.next(), (13, 17, 21, 25))
        self.assertEqual(corners.next(), (31, 37, 43, 49))

    def test_ulam_spiral_corners_upto(self):
        self.assertEqual(to_list(ulam_spiral_corners_upto(1)), [(1, 1, 1, 1)])
        self.assertEqual(to_list(ulam_spiral_corners_upto(3)), [(1, 1, 1, 1), (3, 5, 7, 9)])
        self.assertEqual(to_list(ulam_spiral_corners_upto(5)), [(1, 1, 1, 1), (3, 5, 7, 9), (13, 17, 21, 25)])


def to_list(gen):
    return [x for x in gen]


if __name__ == '__main__':
    unittest.main()
