import unittest

from decorators import *


class ListifyTest(unittest.TestCase):
    @listify
    def range_by_yield(self, start, end, step=1):
        for i in range(start, end, step):
            yield i

    def test_listify(self):
        self.assertEqual(self.range_by_yield(0, 10), range(0, 10))
        self.assertEqual(self.range_by_yield(0, 10, 2), range(0, 10, 2))


if __name__ == '__main__':
    unittest.main()
