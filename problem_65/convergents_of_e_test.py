import unittest
from convergents_of_e import *


class ConvergentsOfETest(unittest.TestCase):
    def test(self):
        self.assertEqual((2, 1), expansion_of_e(1))
        self.assertEqual((3, 1), expansion_of_e(2))
        self.assertEqual((8, 3), expansion_of_e(3))
        self.assertEqual((11, 4), expansion_of_e(4))
        self.assertEqual((19, 7), expansion_of_e(5))
        self.assertEqual((1457, 536), expansion_of_e(10))


if __name__ == '__main__':
    unittest.main()
