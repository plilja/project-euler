from common.ulam_spiral import *
from common.primes import *

SIEVE = PrimeSieve(100000)


def prime_ratio_below(limit):
    corners_seen = 1
    primes_seen = 0
    n = 3
    for corners in ulam_spiral_corners_except_center():
        primes_seen += len(filter(is_prime, corners))
        corners_seen += len(corners)
        if float(primes_seen)/corners_seen < limit:
            return n
        n += 2