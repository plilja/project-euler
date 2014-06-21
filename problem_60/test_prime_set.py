import unittest

from prime_set import *


class PrimeSetTest(unittest.TestCase):
    def test_prime_set(self):
        self.assertEqual(prime_set(2), [3, 7])
        self.assertEqual(prime_set(3), [3, 37, 67])
        self.assertEqual(prime_set(4), [3, 7, 109, 673])

    def test_project_euler(self):
        res = prime_set(5)
        self.assertEqual(res, [13, 5197, 5701, 6733, 8389])
        self.assertEqual(sum(res), 26033)


if __name__ == '__main__':
    unittest.main()
