from math import sqrt, floor


def prime_factors(number):
    largest_possible_prime_factor = int(floor(sqrt(number)))
    for n in range(largest_possible_prime_factor, 1, -1):
        if number % n == 0:
            return prime_factors(n) + prime_factors(number / n)
    return [number]


def largest_prime_factor(number):
    return max(prime_factors(number))