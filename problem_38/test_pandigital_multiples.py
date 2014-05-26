import unittest

from pandigital_multiples import *


class PandigitalMultiplesTest(unittest.TestCase):
    def test_pandigital_multiples(self):
        self.assertTrue((918273645, 9, 5) in pandigital_multiples())
        self.assertTrue((192384576, 192, 3) in pandigital_multiples())

    def test_project_euler(self):
        self.assertEqual(max(map(lambda x: x[0], pandigital_multiples())), 932718654)


if __name__ == '__main__':
    unittest.main()
