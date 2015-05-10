import unittest
import os

from problem_18.maximum_path_sum import maximum_path_sum


class TestMaximumPathSum2(unittest.TestCase):
    def test_project_euler(self):
        infile = open(os.path.join(os.path.dirname(__file__), 'triangle.txt'))
        lines = infile.readlines()
        infile.close()
        triangle = [map(int, line.split(' ')) for line in lines]
        self.assertEqual(7273, maximum_path_sum(triangle))


if __name__ == '__main__':
    unittest.main()
