import unittest

from common.functions import *
from cyclical_figurate_numbers import *


def is_square(num):
    return is_integer(sqrt(num))


def is_heptagonal(num):
    solutions_for_n = solve_second_degree_equation(5, -3, -2 * num)
    return len(filter(is_integer, solutions_for_n)) > 0


def is_octagonal(num):
    solutions_for_n = solve_second_degree_equation(3, -2, -num)
    return len(filter(is_integer, solutions_for_n)) > 0


def atleast_one_is(condition, candidates):
    return len(filter(condition, candidates)) >= 1


class TestCyclicalFigurateNumbers(unittest.TestCase):
    def test_result_has_size_6(self):
        res = cyclical_figurate_number()
        for solution in res:
            self.assertEqual(6, len(solution))

    def test_each_number_in_result_has_4_digits(self):
        for solution in cyclical_figurate_number():
            for num in solution:
                self.assertEqual(len(str(num)), 4)

    def test_each_number_in_represented_in_result(self):
        res = cyclical_figurate_number()
        for solution in res:
            self.assertTrue(atleast_one_is(is_square, solution))
            self.assertTrue(atleast_one_is(is_triangle_number, solution))
            self.assertTrue(atleast_one_is(is_pentagon_number, solution))
            self.assertTrue(atleast_one_is(is_hexagonal_number, solution))
            self.assertTrue(atleast_one_is(is_heptagonal, solution))
            self.assertTrue(atleast_one_is(is_octagonal, solution))

    def test_result_is_cyclical(self):
        res = cyclical_figurate_number()
        for solution in res:
            (a, b, c, d, e, f) = map(str, solution)
            self.assertEqual(f[-2:], a[:2])
            self.assertEqual(a[-2:], b[:2])
            self.assertEqual(b[-2:], c[:2])
            self.assertEqual(c[-2:], d[:2])
            self.assertEqual(d[-2:], e[:2])
            self.assertEqual(e[-2:], f[:2])

    def test_project_euler_ans(self):
        res = cyclical_figurate_number()
        for sol in res:
            self.assertEqual(28684, sum(sol))


if __name__ == '__main__':
    unittest.main()
