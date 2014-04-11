from math import sqrt

from problem_3.large_prime_factor import prime_factors


def num_divisors(factors, number):
    #number = factor1^n1*factor2^n2*factor3^n3...
    #the number of ways we can choose a combination of factors will be the total number of divisors, this number is (n1+1)(n2+1)(n3+1)...
    exponents = []
    for factor in factors:
        exponent = 1
        while number % pow(factor, exponent) == 0:
            exponent += 1
        exponents += [exponent - 1]
    return reduce(lambda x, y: x * (y + 1), exponents, 1)


def num_divisors_for_triangle_num(triangle_num):
    return num_divisors(set(prime_factors(triangle_num)) - {1}, triangle_num)


def triangle_numbers_with_divisors(_num_divisors):
    i = 1
    triangle_num = 1
    while True:
        divisors = num_divisors_for_triangle_num(triangle_num)
        if divisors >= _num_divisors:
            return triangle_num
        i += 1
        triangle_num += i


def triangle_number_with_divisors_brute_force_solution(wanted_num_divisors):
    triangle_num = 1
    i = 1
    while True:
        _num_divisors = 0
        for potential_divisor in range(1, int(sqrt(triangle_num)) + 1):
            if triangle_num % potential_divisor == 0:
                if triangle_num / potential_divisor == potential_divisor:
                    _num_divisors += 1  # square root
                else:
                    _num_divisors += 2  # potential_divisor and triangle_num/potential_divisor are both divisors
        if _num_divisors >= wanted_num_divisors:
            return triangle_num

        i += 1
        triangle_num += i