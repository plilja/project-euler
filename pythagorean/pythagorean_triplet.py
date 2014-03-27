from math import sqrt


def pythagorean_triplet(wanted_sum):
    if wanted_sum <= 0:
        raise ValueError("Wanted sum must be a positive number")
    result = []
    for c in range(wanted_sum - 3, 2, -1):
        for b in range(c - 1, 1, -1):
            a = sqrt(c * c - b * b)
            if a % 1 == 0 and a + b + c == wanted_sum and a < b:
                result += [(int(a), b, c)]

    return result