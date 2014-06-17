from math import fabs

from common.functions import number_as_digits
from common.collection_utils import list_except


def cancelling_fractions():
    res = []
    for n in range(10, 99):
        for d in range(n + 1, 100):
            if d % 10 == 0 or not _has_common_digit(n, d):
                continue

            n_digits = number_as_digits(n)
            d_digits = number_as_digits(d)
            common_digits = set(n_digits) & set(d_digits)
            for common_digit in common_digits:
                n_digits_except_common = list_except(n_digits, n_digits.index(common_digit))
                d_digits_except_common = list_except(d_digits, d_digits.index(common_digit))
                reduced_val = float(next(iter(n_digits_except_common))) / float(next(iter(d_digits_except_common)))
                val = float(n) / float(d)
                if fabs(reduced_val - val) < 0.00000001:
                    res += [(n, d)]
    return res


def _has_common_digit(number_a, number_b):
    number_a_digits = set(number_as_digits(number_a))
    number_b_digits = set(number_as_digits(number_b))
    return len(number_a_digits & number_b_digits) > 0