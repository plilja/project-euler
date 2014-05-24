import unittest

from collection_utils import *


class TestListExcept(unittest.TestCase):
    def test_list_except(self):
        self.assertEqual([1, 2, 3], list_except([1, 2, 3, 4], 3))
        self.assertEqual([1, 2, 4], list_except([1, 2, 3, 4], 2))
        self.assertEqual([2, 3, 4], list_except([1, 2, 3, 4], 0))


if __name__ == '__main__':
    unittest.main()
