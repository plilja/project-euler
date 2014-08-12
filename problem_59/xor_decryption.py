import types
from operator import add
import sys

from common.functions import permutations, pick_from


COMMON_ENGLISH_WORDS = ['of', 'the', 'he', 'she', 'when', 'if', 'was']
ALPHABET = map(chr, range(ord('a'), ord('z') + 1) + range(ord('A'), ord('Z') + 1))
NUMBERS = set(map(str, range(0, 10)))
SPECIAL_CHARACTERS = {'.', ',', ':', ';', '&', '\n', ' ', '(', ')', '[', ']', '$', '!', '?', "'", '"', '-', '=', '%', '@'}
ACCEPTABLE_ENGLISH_CHARACTERS = set(ALPHABET) | SPECIAL_CHARACTERS | NUMBERS


def decrypt(encrypted, key_length):
    if isinstance(encrypted, types.GeneratorType):
        return decrypt(to_list(encrypted), key_length)
    best_solution, best_rank = None, -sys.maxint
    solutions = [_attempt_decrypt_with_key(encrypted, key) for key in generate_keys(key_length)]
    for solution in solutions:
        if rank_as_english(solution) > best_rank:
            best_solution = solution
            best_rank = rank_as_english(solution)
    return best_solution


def to_list(gen):
    return [t for t in gen]


def generate_keys(key_length):
    res = []
    for symbols in pick_from(ALPHABET, key_length):
        res += map(lambda perm: reduce(add, perm), permutations(symbols))
    return res


def _attempt_decrypt_with_key(encrypted, key):
    message = ''
    for i in xrange(len(encrypted)):
        char = chr(encrypted[i] ^ ord(key[i % len(key)]))
        if not char in ACCEPTABLE_ENGLISH_CHARACTERS:
            return ""
        message += char
    return message


def rank_as_english(possibly_in_english):
    lowered = possibly_in_english.lower()
    word_count_found = sum(map(int, map(lambda w: w in lowered, COMMON_ENGLISH_WORDS)))
    return word_count_found