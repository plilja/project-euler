from math import sqrt

from common.functions import is_pandigital


def pandigital_products():
    res = set()
    for product in range(1, int(sqrt(123456789))):
        for multiplicand in range(2, int(sqrt(product))):
            if product % multiplicand == 0:
                pandigital_candidate = int(str(product) + str(multiplicand) + str(product / multiplicand))
                if is_pandigital(pandigital_candidate, 1, 9):
                    res |= {product}
    return res