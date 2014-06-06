from common.functions import *


def is_triangle_number(number):
    #tn = 0.5 * n (n + 1) = 0.5n**2 + 0.5*n
    solutions = solve_second_degree_equation(0.5, 0.5, -number)
    positive_integer_solutions = filter(lambda solution: solution > 0 and is_integer(solution), solutions)
    return len(positive_integer_solutions) > 0


def is_triangle_word(word):
    lower_cased_word = word.lower()
    sum_letters = sum(map(lambda c: ord(c) - ord('a') + 1, lower_cased_word))
    return is_triangle_number(sum_letters)
