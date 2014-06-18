from common.functions import is_palindrome
from common.decorators import listify

def _is_lychrel_number(number, max_iterations):
    if max_iterations == 0:
        return True
    else:
        iteration = number + int(str(number)[::-1])
        if is_palindrome(iteration):
            return False
        else:
            return _is_lychrel_number(iteration, max_iterations - 1)

@listify
def lychrel_numbers_below(limit, max_iterations):
    for i in range(1, limit):
        if _is_lychrel_number(i, max_iterations):
            yield i