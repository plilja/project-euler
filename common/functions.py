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
    if number == 0:
        return [number]
    remainder = number
    res = []
    while remainder != 0:
        res = [remainder % 10] + res
        remainder /= 10
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
    if not isinstance(symbols, set):
        return permutations(set(symbols))
    if not symbols:
        return []
    if len(symbols) == 1:
        return [list(symbols)]
    else:
        result = []
        symbol = symbols.pop()
        sub_permutations = permutations(symbols)
        for sub_permutation in sub_permutations:
            for i in range(0, len(sub_permutation) + 1):
                result += [sub_permutation[0:i] + [symbol] + sub_permutation[i:]]
        return result


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
