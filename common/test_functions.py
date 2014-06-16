import unittest

from functions import *


class FactorialTest(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(1), 1)
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(4), 24)
        self.assertEqual(factorial(5), 120)
        self.assertEqual(factorial(6), 720)
        self.assertEqual(factorial(20), 2432902008176640000)


class FibonacciTest(unittest.TestCase):
    def test_fibonacci(self):
        self.assertEqual(fibonacci(1), 1)
        self.assertEqual(fibonacci(2), 1)
        self.assertEqual(fibonacci(3), 2)
        self.assertEqual(fibonacci(4), 3)
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(12), 144)
        self.assertEqual(fibonacci(40), 102334155)


class NumberAsDigitsTest(unittest.TestCase):
    def test_negative_number(self):
        self.assertEqual(number_as_digits(-1), [-1])
        self.assertEqual(number_as_digits(-10), [-1, 0])

    def test_zero(self):
        self.assertEqual(number_as_digits(0), [0])

    def test_positive_numbers(self):
        self.assertEqual(number_as_digits(1), [1])
        self.assertEqual(number_as_digits(3), [3])
        self.assertEqual(number_as_digits(10), [1, 0])
        self.assertEqual(number_as_digits(101), [1, 0, 1])

    def test_big_input(self):
        self.assertEqual(number_as_digits(901952842935213741234153143120),
                         [9, 0, 1, 9, 5, 2, 8, 4, 2, 9, 3, 5, 2, 1, 3, 7, 4, 1, 2, 3, 4, 1, 5, 3, 1, 4, 3, 1, 2, 0])


class DigitAsNumberTest(unittest.TestCase):
    def test_positive_number(self):
        self.assertEqual(digits_as_num([1, 2, 3]), 123)
        self.assertEqual(digits_as_num([1]), 1)

    def test_zero(self):
        self.assertEqual(digits_as_num([0]), 0)

    def test_negative_number(self):
        self.assertEqual(digits_as_num([-1, 2, 4]), -124)


class IsPandigitTest(unittest.TestCase):
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
        self.assertFalse(is_pandigital(111, 1, 1))
        self.assertFalse(is_pandigital(12334, 1, 4))

    def numbers_with_zero_may_also_be_pandigital(self):
        self.assertTrue(is_pandigital(10, 1, 1))
        self.assertTrue(is_pandigital(100, 1, 1))
        self.assertTrue(is_pandigital(1230456789, 1, 9))
        self.assertTrue(is_pandigital(12030456789, 1, 9))
        self.assertTrue(is_pandigital(120304567890, 1, 9))


class GcdTest(unittest.TestCase):
    def test_gcd(self):
        self.assertEqual(gcd(1, 0), 1)
        self.assertEqual(gcd(1, 1), 1)
        self.assertEqual(gcd(4, 8), 4)
        self.assertEqual(gcd(8, 4), 4)
        self.assertEqual(gcd(6, 9), 3)
        self.assertEqual(gcd(12, 9), 3)
        self.assertEqual(gcd(27, 18), 9)


class PermutationsTest(unittest.TestCase):
    def test_permutations_distinct_elements(self):
        self.assertEqual(sorted(permutations([])), [])
        self.assertEqual(sorted(permutations([5])), [(5,)])
        self.assertEqual(sorted(permutations([1, 2])), sorted([(1, 2), (2, 1)]))
        self.assertEqual(sorted(permutations([1, 2, 3])),
                         sorted([(1, 2, 3), (2, 1, 3), (2, 3, 1), (1, 3, 2), (3, 1, 2), (3, 2, 1)]))

    def test_permutations_duplicate_elements(self):
        self.assertEqual(permutations([1, 1]), [(1, 1)])
        self.assertEqual(sorted(permutations([1, 1, 2])), sorted([(1, 1, 2), (1, 2, 1), (2, 1, 1)]))


class SolveSecondDegreeEquationTest(unittest.TestCase):
    def test_illegal_input(self):
        with self.assertRaises(ValueError):
            solve_second_degree_equation(0, 0, 0)

    def test_no_solutions(self):
        self.assertEqual(solve_second_degree_equation(0, 0, 3), [])

    def test_when_a_is_0_but_not_b(self):
        self.assertEqual(solve_second_degree_equation(0, 1, 0), [0])
        self.assertEqual(solve_second_degree_equation(0, 1, 1), [-1])
        self.assertEqual(solve_second_degree_equation(0, 2, 1), [-0.5])

    def test_when_b_is_0_but_not_a(self):
        self.assertEqual(solve_second_degree_equation(1, 0, 0), [0])
        self.assertEqual(solve_second_degree_equation(1, 0, -4), [2, -2])

    def test_when_c_is_0_but_not_a_or_b(self):
        self.assertEqual(solve_second_degree_equation(1, 1, 0), [0, -1])
        self.assertEqual(solve_second_degree_equation(2, 1, 0), [0, -0.5])
        self.assertEqual(solve_second_degree_equation(1, 2, 0), [0, -2])

    def test_when_all_numbers_are_not_zero(self):
        self.assertEqual(solve_second_degree_equation(1, 1, -2), [1, -2])
        self.assertEqual(solve_second_degree_equation(2, 3, -2), [0.5, -2])

    def test_complex_solutions_are_discarded(self):
        self.assertEqual(solve_second_degree_equation(1, 1, 1), [])
        self.assertEqual(solve_second_degree_equation(1, 2, 4), [])


class IsPentagonNumberTest(unittest.TestCase):
    def test_is_pentagon_number(self):
        self.assertFalse(is_pentagon_number(0))
        self.assertTrue(is_pentagon_number(1))
        self.assertFalse(is_pentagon_number(2))
        self.assertFalse(is_pentagon_number(3))
        self.assertTrue(is_pentagon_number(5))
        self.assertFalse(is_pentagon_number(7))
        self.assertTrue(is_pentagon_number(12))
        self.assertTrue(is_pentagon_number(22))
        self.assertTrue(is_pentagon_number(70))
        self.assertFalse(is_pentagon_number(71))
        self.assertFalse(is_pentagon_number(100))


class IsHexagonNumberTest(unittest.TestCase):
    def test_is_hexagon_number(self):
        self.assertFalse(is_hexagonal_number(0))
        self.assertFalse(is_hexagonal_number(3))
        self.assertFalse(is_hexagonal_number(43))
        self.assertTrue(is_hexagonal_number(1))
        self.assertTrue(is_hexagonal_number(6))
        self.assertTrue(is_hexagonal_number(45))


class IsTriangleNumber(unittest.TestCase):
    def test_is_triangle_number(self):
        self.assertFalse(is_triangle_number(0))
        self.assertFalse(is_triangle_number(2))
        self.assertFalse(is_triangle_number(7))
        self.assertFalse(is_triangle_number(14))
        self.assertTrue(is_triangle_number(1))
        self.assertTrue(is_triangle_number(3))
        self.assertTrue(is_triangle_number(6))
        self.assertTrue(is_triangle_number(15))


class PickFromTest(unittest.TestCase):
    def test_pick_from(self):
        self.assertEqual(pick_from([], 1), [])
        self.assertEqual(pick_from([1], 1), [(1,)])
        self.assertEqual(pick_from([1, 2, 3], 0), [tuple()])
        self.assertEqual(sorted(pick_from([1, 2], 1)), sorted([(1,), (2,)]))
        self.assertEqual(sorted(pick_from([1, 2, 3], 2)), sorted([(1, 2), (1, 3), (2, 3)]))
        self.assertEqual(sorted(pick_from([1, 2, 3, 4], 3)),
                         sorted([(1, 2, 3), (1, 2, 4), (1, 3, 4), (2, 3, 4)]))
        self.assertEqual(pick_from([9, 9, 9], 2), [(9, 9)])


if __name__ == '__main__':
    unittest.main()
