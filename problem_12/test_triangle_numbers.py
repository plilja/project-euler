import unittest

from triangle_numbers import *


class TestTriangleNumbers(unittest.TestCase):
    def test_first_triangle_number_with_1_divisor_is_1(self):
        self.assertEqual(triangle_numbers_with_divisors(1), 1)

    def test_first_triangle_number_with_2_divisors_is_3(self):
        self.assertEqual(triangle_numbers_with_divisors(2), 3)

    def test_first_triangle_number_with_3_divisors_is_6(self):
        self.assertEqual(triangle_numbers_with_divisors(3), 6)

    def test_first_triangle_number_with_4_divisors_is_6(self):
        self.assertEqual(triangle_numbers_with_divisors(4), 6)

    def test_first_triangle_number_with_5_divisors_is_28(self):
        self.assertEqual(triangle_numbers_with_divisors(5), 28)

    def test_first_triangle_number_with_6_divisors_is_28(self):
        self.assertEqual(triangle_numbers_with_divisors(6), 28)

    def test_project_euler_input(self):
        self.assertEqual(triangle_numbers_with_divisors(500), 76576500)


if __name__ == '__main__':
    unittest.main()
