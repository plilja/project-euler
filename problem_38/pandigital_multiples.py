from math import floor

from common.functions import is_pandigital


def pandigital_multiples():
    for n in range(2, 10):
        for i in range(1, pow(10, int(floor(9.0 / n)))):
            pandigit_sum = int(reduce(lambda x, y: x + y, [str(i * j) for j in range(1, n + 1)]))
            if is_pandigital(pandigit_sum, 1, 9):
                yield (pandigit_sum, i, n)
