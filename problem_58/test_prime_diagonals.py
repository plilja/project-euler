import unittest
from prime_diagonals import *

class PrimeDiagonalsTest(unittest.TestCase):
    def test_prime_diagonals(self):
        self.assertEqual(prime_ratio_below(0.7), 3)
        self.assertEqual(prime_ratio_below(0.59), 5)
        self.assertEqual(prime_ratio_below(0.55), 9)
        self.assertEqual(prime_ratio_below(0.5), 11)
        self.assertEqual(prime_ratio_below(0.3), 49)

    @unittest.skip("To slow to run all the time")
    def test_project_euler(self):
        self.assertEqual(prime_ratio_below(0.1), 26241)

if __name__ == '__main__':
    unittest.main()
