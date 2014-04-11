def power_digit_sum(exponent):
    power_of_2 = str(2 ** exponent)
    return sum([int(x) for x in power_of_2])