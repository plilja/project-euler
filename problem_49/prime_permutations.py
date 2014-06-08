from operator import add, and_

from common.primes import *
from common.functions import *


SIEVE = PrimeSieve(10000)


def prime_permutations():
    for digits in pick_from([1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 6, 6, 7, 7, 7, 8, 8, 9, 9, 9], 4):
        prime_permutations = []
        for perm in permutations(digits):
            num = int(reduce(add, map(str, perm)))
            if num < 1000 or \
                    not SIEVE.is_prime(num):
                continue
            prime_permutations += [num]
        combinations = pick_from(list(prime_permutations), 3)
        for combination in combinations:
            if _fills_criteria(combination):
                if 1487 in combination:
                    break
                return combination


def _fills_criteria(combination):
    sorted_combination = sorted(combination)
    if sorted_combination[1] - sorted_combination[0] != sorted_combination[2] - sorted_combination[1]:
        return False
    return reduce(and_, map(SIEVE.is_prime, sorted_combination))