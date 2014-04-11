def _char_value(c):
    assert 'A' <= c <= 'Z'
    return ord(c) - ord('A') + 1


def _value_of_name(name):
    return sum([_char_value(c) for c in name])


def names_scores(names):
    names_sorted = sorted(names)
    res = 0
    for i in xrange(len(names_sorted)):
        res += (i + 1) * _value_of_name(names_sorted[i])
    return res