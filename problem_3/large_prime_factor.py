from common.factors import prime_factors


def largest_prime_factor(number):
    return max(prime_factors(number))