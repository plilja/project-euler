from common.factors import all_proper_divisors


def _abundant_numbers(less_than):
    result = set()
    for n in range(1, less_than):
        if n < sum(all_proper_divisors(n)):
            result |= {n}
    return result


def _can_be_written_as_sum_of_two_abundant_numbers(abundant_numbers, n):
    for j in range(1, n):
        if j in abundant_numbers and n - j in abundant_numbers:
            return True
    return False


def not_sum_of_two_non_abundant(less_than):
    abundant_numbers = _abundant_numbers(less_than)
    result = []
    for i in range(1, less_than):
        if not _can_be_written_as_sum_of_two_abundant_numbers(abundant_numbers, i):
            result += [i]
    return result
