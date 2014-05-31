from itertools import repeat
from math import *
import random


def is_prime(num):
    if not num % 2 or not num % 3:
        return num == 2 or num == 3
    if num < 500000:
        return _is_definitely_prime(num)
    else:
        return is_probably_prime(num, 5) and _is_definitely_prime(num)


def _is_definitely_prime(num):
    if num < 6:
        return num != 1 and num != 4

    if not num % 2 or not num % 3:
        return False
    for i in range(5, int(sqrt(num)) + 1, 6):
        if num % i == 0 or num % (i + 2) == 0:
            return False
    return True


def is_probably_prime(num, k):
    """
    Implementation of the Miller-Rabin primality test.
    """
    if num <= 3 or num % 2 == 0 or num % 3 == 0:
        return _is_definitely_prime(num)

    for i in xrange(k):
        s = 0
        while (num - 1) % (2 ** (s + 1)) == 0:
            s += 1
        d = (num - 1) / (2 ** s)
        assert (num - 1) == 2 ** s * d
        a = random.randint(2, num - 2)
        x = pow_mod(a, d, num)
        if x == 1 or x == num - 1:
            continue
        for _ in xrange(s):
            x = pow_mod(x, 2, num)
            if x == 1:
                return False
            if x == num - 1:
                return is_probably_prime(num, k - i - 2)
        return False
    return True


def pow_mod(num, exponent, modulus):
    if exponent < 100:
        return num ** exponent % modulus
    else:
        subres = pow_mod(num, exponent / 2, modulus) ** 2 % modulus
        if exponent % 2 != 0:
            subres *= num
        return subres % modulus


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

