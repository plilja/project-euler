import unittest

from pandigit import *


class TestPandigitalProducts(unittest.TestCase):
    def test_project_euler(self):
        products = pandigital_products()
        self.assertTrue(7254 in products)
        self.assertEqual(sum(products), 45228)


if __name__ == '__main__':
    unittest.main()
