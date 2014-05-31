from common.functions import permutations


def lexicographic_permutations(symbols):
    _permutations = permutations(set(symbols))
    joined_permutations = [reduce(lambda x, y: x + str(y), permutation, '') for permutation in _permutations]
    return sorted(joined_permutations)
