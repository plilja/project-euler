from common.functions import *


def _find_nearest_n_for_hexagonal_num(num):
    solutions_for_n = solve_second_degree_equation(2, -1, -num)
    positive_solutions_for_n = filter(lambda n: n > 0, solutions_for_n)
    return int(round(positive_solutions_for_n[0]))


def next_tri_pen_and_hex(num):
    n = 1 + _find_nearest_n_for_hexagonal_num(num)
    while True:
        candidate = n * (2 * n - 1)
        if is_triangle_number(candidate) and is_pentagon_number(candidate):
            return candidate
        n += 1
