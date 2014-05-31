from common.primes import *
from common.functions import *


def largest_pandigital_primes(n):
    for i in range(n, 1, -1):
        for pandigital_number in sorted(_all_pandigital_numbers(i), reverse=True):
            if is_prime(pandigital_number):
                return pandigital_number
    raise ValueError("No pandigial prime exists for n=%s" % n)


def _all_pandigital_numbers(n):
    assert n <= 9
    _permutations = permutations(range(1, n + 1))
    _pandigital_numbers_as_strings = map(lambda x: "".join(map(str, x)), _permutations)
    return map(int, _pandigital_numbers_as_strings)


