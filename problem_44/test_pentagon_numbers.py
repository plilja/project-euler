import unittest

from pentagon_numbers import *


class PentagonNumberAndDifferenceTest(unittest.TestCase):
    def test_pentagon_numbers_and_difference(self):
        res = pentagon_numbers_and_difference()
        self.assertEqual(abs(res[0] - res[1]), 5482660)


if __name__ == '__main__':
    unittest.main()
