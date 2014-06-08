import unittest

from self_powers import *


class SelfPowersTest(unittest.TestCase):
    def test_self_powers(self):
        self.assertEqual(self_powers(1), 1)
        self.assertEqual(self_powers(2), 5)
        self.assertEqual(self_powers(3), 32)
        self.assertEqual(self_powers(10), 10405071317)

    def test_project_euler(self):
        self.assertEqual(str(self_powers(1000))[-10:], "9110846700")


if __name__ == '__main__':
    unittest.main()
