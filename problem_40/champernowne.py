_champernownes_constant = ""


def _calculate_champernownes_nth_decimal(length):
    res = []
    curr_length = 0
    i = 1
    while curr_length < length:
        res += [str(i)]
        curr_length += len(res[-1])
        i += 1
    return "".join(res)


def champernownes_nth_decimal(n):
    if len(_champernownes_constant) >= n:
        return int(_champernownes_constant[n - 1])
    global _champernownes_constant
    _champernownes_constant = _calculate_champernownes_nth_decimal(2 * n)
    return champernownes_nth_decimal(n)

