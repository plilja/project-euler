from math import sqrt, log, floor

PSI = (1.0 + sqrt(5)) / 2.0

def n_th_fibonacci_number(n):
    return round(pow(PSI, n) / sqrt(5))

def even_fibonacci(upper_limit):
    return even_fibonacci_mathematical(upper_limit)


def sum_of_nth_first_fibonnaci_numbers(last_even_n):
    return (n_th_fibonacci_number(last_even_n + 2) - 1)


def even_fibonacci_mathematical(upper_limit):
    n = round(log(upper_limit * sqrt(5)) / log(PSI))
    last_even_n = n
    if n_th_fibonacci_number(n) % 2 != 0:
        last_even_n = n - 1
        if n_th_fibonacci_number(n - 1) % 2 != 0:
            last_even_n = n - 2

    return sum_of_nth_first_fibonnaci_numbers(last_even_n) / 2


def even_fibonacci_programmatic(upper_limit):
    return sum(filter(lambda x: x % 2 == 0, fibonacci_numbers_up_to(upper_limit)))


def fibonacci_numbers_up_to(upper_limit):
    if upper_limit <= 0:
        return []
    res = [1, 1]
    while (res[-1] <= upper_limit):
        res += [res[-2] + res[-1]]
    return res[0:-1]
