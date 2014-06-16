import unittest
from prime_digit_replacements import *


class PrimeDigitReplacementsTest(unittest.TestCase):
    def test_no_match(self):
        self.assertEqual(prime_digit_replacements(2, 10), [])

    def test_match_exists(self):
        self.assertEqual(prime_digit_replacements(2, 6), [(13, 23, 43, 53, 73, 83)])

    @unittest.skip("Too slow to run all the time")
    def test_project_euler(self):
        self.assertTrue((121313, 222323, 323333, 424343, 525353, 626363, 828383, 929393) in prime_digit_replacements(6, 8))

if __name__ == '__main__':
    unittest.main()
