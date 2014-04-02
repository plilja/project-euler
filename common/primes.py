from itertools import repeat
from math import sqrt


class PrimeSieve:
    def __init__(self, size):
        self._sieve = self._create_sieve(size)
        self._primes = self._create_primes(self._sieve)

    def _create_sieve(self, size):
        sieve = self._dict_with_all_numbers_initialized_as_primes(size)
        for i in range(2, int(sqrt(size)) + 1):
            if not sieve[i]:
                continue
            for j in range(2 * i, size + 1, i):
                sieve[j] = False
        return sieve

    def _dict_with_all_numbers_initialized_as_primes(self, size):
        return dict(zip(range(2, size + 1), repeat(True, size - 1)))

    def _create_primes(self, sieve):
        primes = []
        for key in sieve.keys():
            if sieve[key]:
                primes += [key]
        return primes

    def is_prime(self, number):
        if number <= 1:
            return False
        if not number in self._sieve:
            raise ValueError('Number not contained in sieve (%s)' % number)
        return self._sieve[number]

    def primes(self):
        return tuple(self._primes)

