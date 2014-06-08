from common.factors import *


def distinct_consecutive_prime_factors(num_factors, num_to_return):
    if num_to_return == 0:
        return []
    i = 2 + num_to_return - 1
    count_found = 0
    while True:
        if len(distinct_prime_factors(i)) == num_factors:
            count_found += 1
            if count_found == num_to_return:
                return range(i, i + num_to_return)
            i -= 1
        else:
            count_found = 0
            i = i + num_to_return


def brute_force_solution(num_factors, num_to_return):
    i = 2
    count_found = 0
    while True:
        if len(distinct_prime_factors(i)) == num_factors:
            count_found += 1
        else:
            count_found = 0
        if count_found == num_to_return:
            return list(reversed(range(i, i - num_to_return, -1)))
        i += 1