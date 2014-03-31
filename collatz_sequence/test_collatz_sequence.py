import unittest

from collatz_sequence import *


class TestCollatzSequenceLength(unittest.TestCase):
    def test_seq_len(self):
        self.assertEqual(collatz_seq_len(1), 1)
        self.assertEqual(collatz_seq_len(2), 2)
        self.assertEqual(collatz_seq_len(4), 3)
        self.assertEqual(collatz_seq_len(8), 4)
        self.assertEqual(collatz_seq_len(16), 5)
        self.assertEqual(collatz_seq_len(5), 6)
        self.assertEqual(collatz_seq_len(10), 7)
        self.assertEqual(collatz_seq_len(20), 8)
        self.assertEqual(collatz_seq_len(40), 9)
        self.assertEqual(collatz_seq_len(13), 10)
        self.assertEqual(collatz_seq_len(1000000), 153)

    def test_longest_collatz_seq(self):
        self.assertEqual(longest_collatz_seq(2), 1)
        self.assertEqual(longest_collatz_seq(5), 3)
        self.assertEqual(longest_collatz_seq(10), 9)
        self.assertEqual(longest_collatz_seq(20), 18)
        self.assertEqual(longest_collatz_seq(50), 27)
        self.assertEqual(longest_collatz_seq(100), 97)
        self.assertEqual(longest_collatz_seq(500), 327)
        self.assertEqual(longest_collatz_seq(1000), 871)

    def test_project_euler_input(self):
        self.assertEqual(longest_collatz_seq(1000000), 837799)


if __name__ == '__main__':
    unittest.main()
