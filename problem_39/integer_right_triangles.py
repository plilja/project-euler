from math import *

_solutions_cache = {}


def integer_right_triangles(length):
    if not _solutions_cache.has_key(length):
        _init_cache(max(1000, length))
    return _solutions_cache[length]


def _init_cache(cache_size):
    for i in range(1, cache_size + 1):
        _solutions_cache[i] = set()
    for c in range(3, cache_size / 2):
        for a in range(1, c):
            b = sqrt(c ** 2 - a ** 2)
            b_rounded = int(round(b))
            length = a + b_rounded + c
            if abs(b - b_rounded) < 0.0000001 and _solutions_cache.has_key(length):
                _solutions_cache[length] |= {tuple(sorted([a, b_rounded, c]))}


