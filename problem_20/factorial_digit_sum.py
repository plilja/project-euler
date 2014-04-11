from common.functions import factorial


def factorial_digit_sum(n):
    return sum([int(x) for x in str(factorial(n))])


