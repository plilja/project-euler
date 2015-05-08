def digit_powers():
    res = []
    for i in range(1, 10):
        j = 0
        while True:
            j += 1
            num = i ** j
            num_digits = len(str(num))
            if num_digits != j:
                break
            res += [num]

    return res