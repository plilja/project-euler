from common.functions import permutations


def _find_cyclical(starting_two_digits, values):
    if not values:
        return [[]]
    head, tail = values[0], values[1:]
    res = []
    for value in head:
        if str(value)[:2] == starting_two_digits:
            sub_results = _find_cyclical(str(value)[-2:], tail)
            res += [[value] + sub_result for sub_result in sub_results]
    return res


def _find_all_cyclical(values):
    res = []
    tail_idx_perms = permutations(range(1, len(values)))
    for idx_perm in tail_idx_perms:
        tail = [values[i] for i in idx_perm]
        head = values[0]
        for value in head:
            res += _find_cyclical(str(value)[-2:], tail + [[value]])
    return res


def cyclical_figurate_number():
    triangle_numbers = [n * (n + 1) / 2 for n in range(45, 141)]
    square_numbers = [n ** 2 for n in range(32, 100)]
    pentagonal_numbers = [n * (3 * n - 1) / 2 for n in range(26, 82)]
    hexagonal_numbers = [n * (2 * n - 1) for n in range(23, 71)]
    heptagonal_numbers = [n * (5 * n - 3) / 2 for n in range(21, 64)]
    octagonal_numbers = [n * (3 * n - 2) for n in range(19, 59)]

    return _find_all_cyclical(
        [triangle_numbers, square_numbers, pentagonal_numbers, hexagonal_numbers, heptagonal_numbers,
         octagonal_numbers])
