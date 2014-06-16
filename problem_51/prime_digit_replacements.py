from common.functions import *
from common.primes import PrimeSieve
from collections import defaultdict

SIEVE = PrimeSieve(10000)


def _replace_prime(digits, way_to_pick):
    digits_copy = list(digits)
    for i in way_to_pick:
        digits_copy[i] = 0
    return digits_as_num(digits_copy)


def _prime_candidates(num_digits):
    for prime in SIEVE.primes_less_than(10 ** num_digits):
        if prime < 10 ** (num_digits - 1):
            continue
        yield prime


def _indices_with_identical_nums(digits):
    digit_and_indices = defaultdict(list)
    for j in xrange(len(digits)):
        digit_and_indices[digits[j]] += [j]
    for val in digit_and_indices.values():
        yield val


def prime_digit_replacements(num_digits, num_primes):
    groups = defaultdict(list)
    for prime in _prime_candidates(num_digits):
        digits = number_as_digits(prime)
        for index_group in _indices_with_identical_nums(digits):
            for num_digits_to_replace in range(1, min(len(index_group) + 1, num_digits)):
                for way_to_pick in pick_from(index_group, num_digits_to_replace):
                    groups[(way_to_pick, _replace_prime(digits, way_to_pick))] += [prime]
    result = []
    for val in groups.values():
        if len(val) >= num_primes:
            result += [tuple(val)]
    return result
