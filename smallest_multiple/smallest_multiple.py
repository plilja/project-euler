from itertools import repeat

from largest_prime_factor.primefactor import prime_factors


def factors_as_dict(divisors_of_number):
    needed_factors_for_number = dict(zip(divisors_of_number, repeat(0, len(divisors_of_number))))
    for needed_factor in divisors_of_number:
        needed_factors_for_number[needed_factor] += 1
    return needed_factors_for_number


def smallest_multiple(numbers):
    total_needed_factors = {}
    factors_of_numbers = map(prime_factors, numbers)

    for factors_of_number in factors_of_numbers:
        factors_of_number_dict = factors_as_dict(factors_of_number)
        for needed_factor in factors_of_number:
            if needed_factor in total_needed_factors:
                total_needed_factors[needed_factor] = max(total_needed_factors[needed_factor],
                                                          factors_of_number_dict[needed_factor])
            else:
                total_needed_factors[needed_factor] = factors_of_number_dict[needed_factor]

    factors_to_exponents = map(lambda x: pow(x[0], x[1]), total_needed_factors.items())
    return reduce(lambda x, y: x * y, factors_to_exponents, 1)
