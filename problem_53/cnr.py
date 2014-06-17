from common.functions import binomial_coefficient


def cnr_larger_than_brute_force(max_n, num_to_exceed):
    res = 0
    for n in range(1, max_n + 1):
        for k in range(1, n + 1):
            if binomial_coefficient(n, k) >= num_to_exceed:
                res += 1
    return res


def cnr_larger_than(max_n, num_to_exceed):
    """
    Uses Pascal's triangle to find the solutions.
    """
    prev_row = [1, 0]
    res = 0
    for n in range(1, max_n + 1):
        curr_row = []
        for k in range(0, n + 1):
            curr_row += [prev_row[k - 1] + prev_row[k]]
            if curr_row[-1] >= num_to_exceed:
                res += 1
        curr_row += [0]
        prev_row = curr_row
    return res