import operator
from itertools import repeat
from math import *


def factorial(n):
    return reduce(operator.mul, range(1, n + 1), 1)


def fibonacci(n):
    (fa, fb) = (1, 1)
    res = 1
    for i in range(2, n):
        res = fa + fb
        (fa, fb) = (fb, res)
    return res


def number_as_digits(number):
    if number < 0:
        negated_res = number_as_digits(-number)
        negated_res[0] *= -1
        return negated_res
    return map(int, str(number))


def digits_as_num(digits):
    sign = int(copysign(1, digits[0]))
    res = 0
    power = 1
    for digit in reversed(digits):
        res += sign * power * abs(digit)
        power *= 10
    return res


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


def is_pandigital(num, start, end):
    values = dict(zip(range(start, end + 1), repeat(0, end - start + 1)))
    for digit in number_as_digits(num):
        if values.has_key(digit):
            values[digit] += 1
    return reduce(operator.and_, map(lambda x: x == 1, values.values()))


def permutations(symbols):
    if not symbols:
        return []
    if len(symbols) == 1:
        return [tuple(symbols)]
    else:
        result = set()
        symbol = symbols[0]
        sub_permutations = permutations(symbols[1:])
        for sub_permutation in sub_permutations:
            for i in range(0, len(sub_permutation) + 1):
                result |= {sub_permutation[0:i] + (symbol,) + sub_permutation[i:]}
        return list(result)


def solve_second_degree_equation(a, b, c):
    """
    Solves a second degree equation of the form ax**2 + bx + c = 0.
    Returns real valued solutions as a list. Complex solutions are ignored.
    """
    if (a, b, c) == (0, 0, 0):
        raise ValueError("Infinite number of solutions")
    if (a, b) == (0, 0):
        return []
    if a == 0:
        return [-float(c) / float(b)]
    p = float(b) / float(a)
    q = float(c) / float(a)
    d = (p / 2) ** 2
    if d - q == 0:
        return [-p / 2]
    if d - q > 0:
        return [-p / 2 + sqrt(d - q), -p / 2 - sqrt(d - q)]
    else:
        return []


def is_integer(float_number):
    return abs(float_number - round(float_number)) < 0.0000001


def is_pentagon_number(number):
    # pn = n(3n-1)/2 = 1.5n**2 -0.5n
    return _second_degree_equation_has_positive_int_solution(1.5, -0.5, -number)


def is_hexagonal_number(number):
    # hn = n(2n - 1) = 2n**2 - n
    return _second_degree_equation_has_positive_int_solution(2, -1, -number)


def is_triangle_number(number):
    # tn = 0.5 * n (n + 1) = 0.5n**2 + 0.5*n
    return _second_degree_equation_has_positive_int_solution(0.5, 0.5, -number)


def _second_degree_equation_has_positive_int_solution(a, b, c):
    solutions = solve_second_degree_equation(a, b, c)
    positive_integer_solutions = filter(lambda solution: solution > 0 and is_integer(solution), solutions)
    return len(positive_integer_solutions) > 0


def pick_from(values, num_to_pick):
    if len(values) < num_to_pick:
        return []
    if len(values) == num_to_pick:
        return [tuple(values)]
    if num_to_pick == 0:
        return [tuple()]
    first = values[0]
    result_with_first = map(lambda x: (first,) + x, pick_from(values[1:], num_to_pick - 1))
    result_without_first = pick_from(values[1:], num_to_pick)
    return list(set(result_with_first + result_without_first))

def binomial_coefficient(n, k):
    diff = n - k
    numerator = 1
    for j in range(n, diff, -1):
        numerator *= j
    return numerator/factorial(k)

def is_palindrome(number):
    return str(number) == str(number)[::-1]
