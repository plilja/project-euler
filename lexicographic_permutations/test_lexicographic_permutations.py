import unittest

from lexicographic_permutations import *


class TestLexicographicPermutations(unittest.TestCase):
    def test_permutate_1_input_symbol(self):
        self.assertEqual(lexicographic_permutations([1]), ['1'])
        self.assertEqual(lexicographic_permutations([0]), ['0'])
        self.assertEqual(lexicographic_permutations([2]), ['2'])

    def test_permutate_2_input_symbols(self):
        self.assertEqual(lexicographic_permutations([0, 1]), ['01', '10'])
        self.assertEqual(lexicographic_permutations([1, 0]), ['01', '10'])
        self.assertEqual(lexicographic_permutations([2, 1]), ['12', '21'])

    def test_permutate_3_input_symbols(self):
        self.assertEqual(lexicographic_permutations([0, 1, 2]), ['012', '021', '102', '120', '201', '210'])
        self.assertEqual(lexicographic_permutations([2, 1, 0]), ['012', '021', '102', '120', '201', '210'])
        self.assertEqual(lexicographic_permutations([2, 3, 0]), ['023', '032', '203', '230', '302', '320'])

    def test_permutate_4_input_symbols(self):
        self.assertEqual(lexicographic_permutations([0, 1, 2, 3]),
                         ['0123', '0132', '0213', '0231', '0312', '0321', '1023', '1032', '1203', '1230', '1302',
                          '1320', '2013', '2031', '2103', '2130', '2301', '2310', '3012', '3021', '3102', '3120',
                          '3201', '3210'])

    @unittest.skip("A little bit slow to run all the time")
    def test_project_euler_input(self):
        self.assertEqual(lexicographic_permutations(range(0, 10))[1000000 - 1], '2783915460')


if __name__ == '__main__':
    unittest.main()
