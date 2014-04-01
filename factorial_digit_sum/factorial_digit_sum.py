import operator


def factorial_digit_sum(n):
    return sum([int(x) for x in str(factorial(n))])


def factorial(n):
    return reduce(operator.mul, range(1, n + 1), 1)