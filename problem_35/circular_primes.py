from operator import and_

from common.primes import PrimeSieve


def circular_primes(upper_limit):
    sieve = PrimeSieve(upper_limit)
    return [x for x in sieve.primes() if _is_circular_prime(x, sieve)]


def _is_circular_prime(num, sieve):
    return reduce(and_, map(sieve.is_prime, _rotations(num)))


def _rotations(num):
    num_str = str(num)
    return [num] + [int(num_str[-i:] + num_str[0:-i]) for i in range(1, len(num_str))]

