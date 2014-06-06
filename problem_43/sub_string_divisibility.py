from operator import add

from common.decorators import listify

from common.functions import permutations


_DIVISORS = [2, 3, 5, 7, 11, 13, 17]


def find_candidates():
    candidates_without_zero = permutations([1, 2, 3, 4, 5, 6, 7, 8, 9])
    candidates_without_five = permutations([0, 1, 2, 3, 4, 6, 7, 8, 9])
    for candidate in candidates_without_zero:
        if candidate[3] % 2 == 0:
            yield candidate[0:5] + [0] + candidate[5:]
    for candidate in candidates_without_five:
        if candidate[0] != 0 and candidate[3] % 2 == 0:
            yield candidate[0:5] + [5] + candidate[5:]


@listify
def sub_string_divisibility():
    _candidates = find_candidates()
    for candidate in _candidates:
        match = True
        for i in range(0, 7):
            if (100 * candidate[i + 1] + 10 * candidate[i + 2] + candidate[i + 3]) % _DIVISORS[i] != 0:
                match = False
                break
        if match:
            yield int(reduce(add, map(str, candidate)))
