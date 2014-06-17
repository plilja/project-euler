import unittest
from operator import mul

from cancelling import *
from common.functions import gcd


class TestCancellingFraction(unittest.TestCase):
    def test_cancelling(self):
        self.assertTrue((49, 98) in cancelling_fractions())
        self.assertTrue((16, 64) in cancelling_fractions())
        self.assertTrue((26, 65) in cancelling_fractions())
        self.assertTrue((19, 95) in cancelling_fractions())
        self.assertEqual(4, len(cancelling_fractions()))

    def test_project_euler(self):
        numerator = reduce(mul, [x[0] for x in cancelling_fractions()])
        denominator = reduce(mul, [x[1] for x in cancelling_fractions()])
        self.assertEqual(denominator / gcd(numerator, denominator), 100)


if __name__ == '__main__':
    unittest.main()
