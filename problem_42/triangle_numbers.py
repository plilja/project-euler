from common.functions import *


def is_triangle_word(word):
    lower_cased_word = word.lower()
    sum_letters = sum(map(lambda c: ord(c) - ord('a') + 1, lower_cased_word))
    return is_triangle_number(sum_letters)
