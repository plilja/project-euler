def find_start_and_step(start, multiples):
    # if a is divisible by 3 then the digit sum of a must also be divisible by 3.
    step = 3 if 3 in multiples else 1
    while step == 3 and start % 3 != 0:
        return find_start_and_step(start + 1, multiples)
    return start, step


def multiple_with_same_digits(multiples):
    j = 1
    max_multiple = max(multiples)
    while True:
        j *= 10
        (start, step) = find_start_and_step(j, multiples)

        upper_limit = j * 10 / max_multiple  # The number and the multiple of the number must have the same number of digits
        for i in range(start, upper_limit, step):
            digits_i = sorted(str(i))
            found = True
            for mul in multiples:
                if digits_i != sorted(str(mul * i)):
                    found = False
                    break
            if found:
                return i