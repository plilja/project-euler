from math import sqrt, floor


def distinct_prime_factors(number):
    return set(prime_factors(number))


def prime_factors(number):
    """
    Returns list of all prime factors of a number.
    """
    largest_possible_prime_factor = int(floor(sqrt(number)))
    for n in range(largest_possible_prime_factor, 1, -1):
        if number % n == 0:
            return prime_factors(n) + prime_factors(number / n)
    return [number]


def prime_factorization(number):
    """
    Returns factorization of number as set we're each entry contains the factor
    and the power to which the factor fits in the number.

    Example prime_factorization(12) = {2:2, 3:1}
    """
    if number == 1:
        return {1: 1}
    _prime_factors = prime_factors(number)
    prime_factors_with_exponents = dict(zip(_prime_factors, [1 for i in _prime_factors]))
    for prime_factor in _prime_factors:
        i = 1
        while number % prime_factor ** i == 0:
            i += 1
        prime_factors_with_exponents[prime_factor] = i - 1
    return prime_factors_with_exponents


def all_divisors(number, known_factorization=None):
    if known_factorization:
        _prime_factorization = known_factorization
    else:
        _prime_factorization = prime_factorization(number)
    result = set()
    for prime_factor in _prime_factorization.keys():
        if number == 1:
            continue
        prime_factorization_except_divisor = {k: _prime_factorization[k] for k in _prime_factorization if
                                              k != prime_factor}
        all_factors_of_number_divided_by_prime_factor = all_divisors(
            number / prime_factor ** _prime_factorization[prime_factor],
            prime_factorization_except_divisor)
        for i in xrange(_prime_factorization[prime_factor] + 1):
            result |= {prime_factor ** i * x for x in all_factors_of_number_divided_by_prime_factor}
    return {1} | result


def all_proper_divisors(n):
    return all_divisors(n) - {n} | {1}
