import unittest

from pandigit import *


class TestIsPandigit(unittest.TestCase):
    def test_not_all_numbers_used(self):
        self.assertFalse(is_pandigital(1, 1, 2))
        self.assertFalse(is_pandigital(2, 1, 1))
        self.assertFalse(is_pandigital(2, 1, 2))

    def test_all_numbers_used_once(self):
        self.assertTrue(is_pandigital(1, 1, 1))
        self.assertTrue(is_pandigital(15234, 1, 5))
        self.assertTrue(is_pandigital(123456789, 1, 9))
        self.assertTrue(is_pandigital(923456781, 1, 9))

    def test_some_numbers_used_more_than_once(self):
        self.assertFalse(is_pandigital(11, 1, 1))
        self.assertFalse(is_pandigital(12334, 1, 4))

    def numbers_with_zero_may_also_be_pandigital(self):
        self.assertTrue(is_pandigital(10, 1, 1))
        self.assertTrue(is_pandigital(100, 1, 1))
        self.assertTrue(is_pandigital(1230456789, 1, 9))
        self.assertTrue(is_pandigital(12030456789, 1, 9))
        self.assertTrue(is_pandigital(120304567890, 1, 9))


class TestPandigitalProducts(unittest.TestCase):
    def test_project_euler(self):
        products = pandigital_products()
        self.assertTrue(7254 in products)
        self.assertEqual(sum(products), 45228)


if __name__ == '__main__':
    unittest.main()
