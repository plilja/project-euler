def _permutations(symbols):
    if len(symbols) <= 1:
        return [list(symbols)]
    else:
        result = []
        symbol = symbols.pop()
        sub_permutations = _permutations(symbols)
        for sub_permutation in sub_permutations:
            for i in range(0, len(sub_permutation) + 1):
                result += [sub_permutation[0:i] + [symbol] + sub_permutation[i:]]
        return result


def lexicographic_permutations(symbols):
    permutations = _permutations(set(symbols))
    joined_permutations = [reduce(lambda x, y: x + str(y), permutation, '') for permutation in permutations]
    return sorted(joined_permutations)
