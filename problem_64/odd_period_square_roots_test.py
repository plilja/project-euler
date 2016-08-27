import unittest
from odd_period_square_roots import *

class PeriodLengthTst(unittest.TestCase):
    def test_period_length(self):
        self.assertEqual(1, period_length(2))
        self.assertEqual(2, period_length(3))
        self.assertEqual(1, period_length(5))
        self.assertEqual(2, period_length(6))
        self.assertEqual(4, period_length(7))
        self.assertEqual(2, period_length(8))
        self.assertEqual(1, period_length(10))
        self.assertEqual(2, period_length(11))
        self.assertEqual(2, period_length(12))
        self.assertEqual(5, period_length(13))
        self.assertEqual(4, period_length(23))

if __name__ == '__main__':
    unittest.main()
