def sum_digit_powers(power):
    res = []

    computation_cache = {digit: digit ** power for digit in range(0, 10)}

    for number in range(10, pow(10, power + 1)):
        first_digit_power = computation_cache[number % 10]
        remaining_digits = computation_cache[number / 10]
        power_number_sum = first_digit_power + remaining_digits
        computation_cache[number] = power_number_sum
        if number == power_number_sum:
            res += [number]
    return res

