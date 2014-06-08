from common.primes import PrimeSieve

SIEVE = PrimeSieve(1000)


def consecutive_prime_sum_less_than(num):
    (longest_count, longest_prime) = (0, 2)
    primes_less_than_num = SIEVE.primes_less_than(num)
    for i in range(0, len(primes_less_than_num)):
        count = 0
        _sum = 0
        for prime in primes_less_than_num[i:]:
            _sum += prime
            count += 1
            if _sum > num:
                break
            if count > longest_count and SIEVE.is_prime(_sum):
                (longest_count, longest_prime) = (count, _sum)

    return longest_prime
