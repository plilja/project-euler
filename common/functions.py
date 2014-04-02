import operator


def factorial(n):
    return reduce(operator.mul, range(1, n + 1), 1)