import unittest

from fraction_expansions import *


class FractionExpansionsTest(unittest.TestCase):
    def test_fraction_expansions(self):
        self.assertEqual(fraction_expansions(1), [(3, 2)])
        self.assertEqual(fraction_expansions(2), [(3, 2), (7, 5)])
        self.assertEqual(fraction_expansions(3), [(3, 2), (7, 5), (17, 12)])
        self.assertEqual(fraction_expansions(4), [(3, 2), (7, 5), (17, 12), (41, 29)])

    def test_project_euler(self):
        count = 0
        for num, den in fraction_expansions(1000):
            if len(str(num)) > len(str(den)):
                count += 1
        self.assertEqual(count, 153)


if __name__ == '__main__':
    unittest.main()
