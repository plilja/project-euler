
def multiples_of_3_and_5(max_limit):
    return sum(filter(is_multiple_of_3_or_5, range(3, max_limit)))

def is_multiple_of_3_or_5(x):
    return x % 3 == 0 or x % 5 == 0
