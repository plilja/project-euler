from math import sqrt


def is_pandigital(num, start, end):
    unused_values = set(range(start, end + 1)) | {0}
    for digit_set in map(lambda x: {int(x)}, str(num)):
        diff = unused_values ^ digit_set
        intersect = unused_values & digit_set
        unused_values = unused_values - intersect | diff
    return unused_values <= {0}


def pandigital_products():
    res = set()
    for product in range(1, int(sqrt(123456789))):
        for multiplicand in range(2, int(sqrt(product))):
            if product % multiplicand == 0:
                pandigital_candidate = int(str(product) + str(multiplicand) + str(product / multiplicand))
                if is_pandigital(pandigital_candidate, 1, 9):
                    res |= {product}
    return res