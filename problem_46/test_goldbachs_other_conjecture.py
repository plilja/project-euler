import unittest

from goldbachs_other_conjecture import *


class GoldbachsOtherConjectureTest(unittest.TestCase):
    def test_goldbachs_other_conjecture(self):
        self.assertEqual(goldbachs_other_conjecture(), 5777)


if __name__ == '__main__':
    unittest.main()
