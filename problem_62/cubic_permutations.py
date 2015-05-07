from common.functions import *


def cubic_permutations(wanted):
    i = 0
    numbers = {}
    smallest_cube_for_number = {}
    last_len = 1
    while True:
        i += 1
        num = i ** 3
        digits = number_as_digits(num)
        if len(digits) != last_len:
            j = 0
            matches = []
            for k, v in numbers.iteritems():
                j += 1
                if v == wanted:
                    matches += [smallest_cube_for_number[k]]
            if matches:
                return min(matches)
            last_len = len(digits)
            numbers = {}
            smallest_cube_for_number = {}
        key = reduce(operator.add, map(str, sorted(digits)))
        if not key in numbers:
            numbers[key] = 0
            smallest_cube_for_number[key] = num
        numbers[key] += 1




