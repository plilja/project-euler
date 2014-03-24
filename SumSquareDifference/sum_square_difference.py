def sum_square_difference(n):
    return sum_square_difference_mathematical(n)


def sum_square_difference_programmatic(n):
    sum_of_squares = sum(map(lambda x: pow(x, 2), range(1, n + 1)))
    square_om_sum = pow(sum(range(1, n + 1)), 2)
    return square_om_sum - sum_of_squares


def sum_square_difference_mathematical(n):
    sum_of_squares = n * (n + 1) * (2 * n + 1) / 6
    sum = n * (n + 1) / 2
    square_of_sums = sum * sum
    return square_of_sums - sum_of_squares
