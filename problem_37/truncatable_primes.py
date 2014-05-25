from common.primes import PrimeSieve


def truncatable_primes():
    sieve = PrimeSieve(1000000)
    res = []
    for prime in sieve.primes()[4:]:  # The 5th prime is 11, the first prime greater than 10
        if _is_truncatable_from_both_directions(prime, sieve):
            res += [prime]
        if len(res) >= 11:  # According to problem description there are exactly 11 truncatable primes
            break
    return res


def _is_truncatable_from_both_directions(number, sieve):
    return _is_truncatable_from_one_direction(number, sieve, lambda x: x / 10) and \
           _is_truncatable_from_one_direction(number, sieve, lambda x: int(str(x)[1:]))


def _is_truncatable_from_one_direction(number, sieve, truncator):
    if number <= 9:
        return sieve.is_prime(number)
    else:
        return sieve.is_prime(number) and _is_truncatable_from_one_direction(truncator(number), sieve, truncator)

