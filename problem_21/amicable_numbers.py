from common.factors import all_proper_divisors


def sum_of_divisors(n, sum_of_divisors_cache):
    if n in sum_of_divisors_cache:
        return sum_of_divisors_cache[n]
    else:
        sum_of_divisors = sum(all_proper_divisors(n))
        sum_of_divisors_cache[n] = sum_of_divisors
        return sum_of_divisors


def amicable_numbers_less_than(n):
    result = []
    sum_of_divisors_cache = {}
    for i in range(2, n):
        sum_of_divisors_i = sum_of_divisors(i, sum_of_divisors_cache)
        if sum_of_divisors_i != i and sum_of_divisors(sum_of_divisors_i, sum_of_divisors_cache) == i:
            result += [i]
    return result