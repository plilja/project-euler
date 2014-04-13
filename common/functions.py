import operator


def factorial(n):
    return reduce(operator.mul, range(1, n + 1), 1)


def fibonacci(n):
    (fa, fb) = (1, 1)
    res = 1
    for i in range(2, n):
        res = fa + fb
        (fa, fb) = (fb, res)
    return res


def number_as_digits(number):
    if number == 0:
        return [number]
    remainder = number
    res = []
    while remainder != 0:
        res = [remainder % 10] + res
        remainder /= 10
    return res