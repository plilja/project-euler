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
        for i in range(3, int(sqrt(size)) + 1, 2):
            if not sieve[i / 2]:
                continue
            for j in range(3 * i, size + 1, 2 * i):
                sieve[j / 2] = False
        return sieve

    def _dict_with_all_numbers_initialized_as_primes(self, size):
        return dict(zip(range(1, size / 2), repeat(True, size / 2 - 1)))

    def _create_primes(self, sieve):
        primes = []
        if self._size > 2:
            primes += [2]
        for key in sieve.keys():
            if sieve[key]:
                primes += [key * 2 + 1]
        return primes

    def is_prime(self, number):
        if number <= 1:
            return False
        elif number % 2 == 0:
            return number == 2
        if not number / 2 in self._sieve:
            self.grow(2 * number)
        return self._sieve[number / 2]

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
        return res

    def current_size(self):
        return self._size

    def grow(self, new_size):
        self._initialize_to_size(new_size)

