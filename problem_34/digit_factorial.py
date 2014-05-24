from common.functions import factorial
from common.functions import number_as_digits


def digit_factorial():
    res = []
    for i in range(3, 100000):
        if i == sum(map(factorial, number_as_digits(i))):
            res += [i]
    return res