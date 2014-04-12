from common.primes import PrimeSieve

_prime_sieve = PrimeSieve()


def quadratic_primes(n):
    longest_seq = -1
    best_values = (0, 0)
    for b in _prime_sieve.primes_less_than(n):
        if b >= n:
            break
        for a in range(-b + 1, n):
            prime_seq_i = quadratic_primes_seq(a, b)
            if len(prime_seq_i) > longest_seq:
                best_values = (a, b)
                longest_seq = len(prime_seq_i)

    return best_values


def quadratic_primes_seq(a, b, i=0):
    val_i = i ** 2 + a * i + b
    if _prime_sieve.is_prime(val_i):
        return [val_i] + quadratic_primes_seq(a, b, i + 1)
    else:
        return []