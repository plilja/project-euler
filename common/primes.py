from itertools import repeat
from math import sqrt


class PrimeSieve:
    def __init__(self, size=1000):
        self._initialize_to_size(size)

    def _initialize_to_size(self, size):
        self._size = size
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
            self.grow(2 * number)
        return self._sieve[number]

    def primes(self):
        return self._primes

    def primes_less_than(self, n):
        if n < self._size:
            self.grow(2 * n)
        res = []
        for prime in self.primes():
            if prime >= n:
                break
            res += [prime]
        return tuple(res)

    def current_size(self):
        return self._size

    def grow(self, new_size):
        self._initialize_to_size(new_size)

