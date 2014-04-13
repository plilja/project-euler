import unittest

from coin_sums import *


class TestCoinSums(unittest.TestCase):
    def test_coin_sums(self):
        self.assertEqual(coin_sums(0), 1)
        self.assertEqual(coin_sums(1), 1)
        self.assertEqual(coin_sums(2), 2)  #2x1, 1x2
        self.assertEqual(coin_sums(3), 2)  #3x1, 1x1+1x2
        self.assertEqual(coin_sums(4), 3)  #4x1, 2x1+2, 2x2
        self.assertEqual(coin_sums(5), 4)  #5x1, 3x1+2, 1x1+2x2, 1x5
        self.assertEqual(coin_sums(10), 11)
        self.assertEqual(coin_sums(20), 41)
        self.assertEqual(coin_sums(100), 4563)

    def test_project_euler_input(self):
        self.assertEqual(coin_sums(200), 73682)


if __name__ == '__main__':
    unittest.main()
