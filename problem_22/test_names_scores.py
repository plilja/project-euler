import unittest
import os

from names_scores import *


class TestNamesScores(unittest.TestCase):
    def test_names_scores(self):
        self.assertEqual(names_scores(['C']), 3)
        self.assertEqual(names_scores(['C', 'C']), 9)
        self.assertEqual(names_scores(['C', 'O']), 33)
        self.assertEqual(names_scores(['O', 'C']), 33)
        self.assertEqual(names_scores(['C', 'L', 'O']), 72)
        self.assertEqual(names_scores(['O', 'C', 'L']), 72)
        self.assertEqual(names_scores(['COLIN']), 53)
        self.assertEqual(names_scores(['NILOC']), 53)
        self.assertEqual(names_scores(['COLIN', 'NILOC']), 159)

    def test_project_euler_input(self):
        infile = open(os.path.join(os.path.dirname(__file__), 'names.txt'))
        names = infile.read().replace('"', '').split(",")
        infile.close()
        self.assertEqual(names_scores(names), 871198282)

    if __name__ == '__main__':
        unittest.main()
