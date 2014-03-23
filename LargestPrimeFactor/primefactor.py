from math import sqrt, floor


def prime_factors(number):
    _prime_factors = []
    largest_possible_prime_factor = int(floor(sqrt(number)))
    for n in range(largest_possible_prime_factor, 1, -1):
        if number % n == 0:
            _prime_factors += prime_factors(n)
    if not _prime_factors:
        return [number]
    else:
        return _prime_factors


def largest_prime_factor(number):
    return max(prime_factors(number))