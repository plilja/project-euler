from common.functions import number_as_digits


def powers(a, b):
    res = 1
    for i in range(1, a + 1):
        for j in range(1, b + 1):
            res = max(res, sum(number_as_digits(i ** j)))
    return res