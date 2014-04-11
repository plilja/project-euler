def reciprocal_cycles(upper_limit):
    max_val = -1
    max_i = -1
    for i in range(1, upper_limit + 1):
        i_reciprocal_cycle_len = _reciprocal_cycle_length(i)
        if i_reciprocal_cycle_len > max_val:
            max_val = i_reciprocal_cycle_len
            max_i = i
    return max_i


def _reciprocal_cycle_length(n):
    """
    Finds reciprocal cycles by using long division and looking for remainders in the division that has been seen before.
    If a remainder has been seen before there must be a cycle.
    """
    remainder = 10 * (1 % n)
    seen_remainders_and_offset = {}
    offset = 0
    while remainder not in seen_remainders_and_offset:
        seen_remainders_and_offset[remainder] = offset
        if remainder % n == 0:
            return 0
        else:
            remainder = 10 * (remainder % n)
        offset += 1
    return offset - seen_remainders_and_offset[remainder]