def multiples_of_x(limit_excl, x):
    limit_incl = limit_excl - 1
    num_x_divisable = limit_incl / x
    return int(x * (1.0 + num_x_divisable) * (num_x_divisable / 2.0))


def multiples_of_3_and_5(limit_excl):
    return multiples_of_x(limit_excl, 3) + multiples_of_x(limit_excl, 5) - multiples_of_x(limit_excl, 15)


def multiples_of_3_and_5_programmatic(limit_excl):
    return sum(filter(is_multiple_of_3_or_5, range(3, limit_excl)))


def is_multiple_of_3_or_5(x):
    return x % 3 == 0 or x % 5 == 0
