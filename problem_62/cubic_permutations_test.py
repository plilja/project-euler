import unittest

from cubic_permutations import cubic_permutations


class CubicPermutationsTest(unittest.TestCase):
    def test_cubic_permutations_sample_input(self):
        self.assertEqual(41063625, cubic_permutations(3))

    def test_answer(self):
        self.assertEqual(127035954683, cubic_permutations(5))


if __name__ == '__main__':
    unittest.main()
