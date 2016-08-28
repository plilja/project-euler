from common.functions import *


def expansion_of_e(n):
    xs = [2]
    j = 2
    for i in range(2, n + 1):
        if i % 3 == 0:
            xs += [j]
            j += 2
        else:
            xs += [1]

    a = 0
    b = 1
    for x in reversed(xs[1:]):
        a += x * b
        (a, b) = (b, a)

    a += b * xs[0]
    d = gcd(a, b)
    return a / d, b / d


def convergents_of_e(n):
    (a, b) = expansion_of_e(n)
    return sum(number_as_digits(a))


if __name__ == '__main__':
    print(convergents_of_e(100))
