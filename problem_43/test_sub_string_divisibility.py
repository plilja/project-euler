import unittest

from sub_string_divisibility import *


class SubStringDivisibilityTest(unittest.TestCase):
    def test_substring_divisibility(self):
        result = sub_string_divisibility()
        self.assertTrue(1406357289 in result)
        self.assertTrue(1460357289 in result)
        self.assertTrue(4106357289 in result)
        self.assertTrue(4160357289 in result)
        self.assertTrue(1430952867 in result)
        self.assertTrue(4130952867 in result)
        self.assertEqual(sum(result), 16695334890)


if __name__ == '__main__':
    unittest.main()
