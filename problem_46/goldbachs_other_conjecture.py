from math import sqrt

from common.primes import PrimeSieve
from common.functions import is_integer


SIEVE = PrimeSieve(10000)


def goldbachs_other_conjecture():
    i = 9
    while True:
        if not SIEVE.is_prime(i):
            if _breaks_conjecture(i):
                return i
        i += 2


def _breaks_conjecture(num):
    for prime in SIEVE.primes():
        if prime > num:
            break
        if is_integer(sqrt((num - prime) / 2)):
            return False
    return True
