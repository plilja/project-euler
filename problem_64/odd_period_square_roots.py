from common.functions import *


def period_length(n):
    a = 1
    r = sqrt(n)
    if int(r)**2 == n:
        return 0
    b = int(r)
    seen = set()
    ans = 0
    while (a, b) not in seen:
        seen.add((a, b))
        ans += 1
        c = n - b*b
        a_new = c / gcd(a, c)
        i = 1
        while r + b - a_new * (i + 1) > 0:
            i += 1
        b = abs(b - i * a_new)
        a = a_new
    return ans


def odd_period_square_roots(lim):
    r = 0
    for i in range(1, lim + 1):
        if period_length(i) % 2 == 1:
            r += 1
    return r


if __name__ == '__main__':
    print(odd_period_square_roots(10000))


