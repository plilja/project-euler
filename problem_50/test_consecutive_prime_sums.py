import unittest

from consecutive_prime_sums import *


class ConsecutivePrimeSumsTest(unittest.TestCase):
    def test_consecutive_prime_sums(self):
        self.assertEqual(consecutive_prime_sum_less_than(100), 41)
        self.assertEqual(consecutive_prime_sum_less_than(1000), 953)
        self.assertEqual(consecutive_prime_sum_less_than(10000), 9521)
        self.assertEqual(consecutive_prime_sum_less_than(100000), 92951)

    @unittest.skip("A little bit slow to run all the time")
    def test_project_euler(self):
        self.assertEqual(consecutive_prime_sum_less_than(1000000), 997651)


if __name__ == '__main__':
    unittest.main()
