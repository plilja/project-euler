import operator

from matrix import Matrix


def _calc_row_product(numbers, start_idx, end_idx_excl):
    return reduce(operator.mul, numbers[start_idx:end_idx_excl], 1)


def _calculate_max_product_for_vector(vector, length):
    max_val = -1
    for j in xrange(len(vector) - length + 1):
        product = _calc_row_product(vector, j, j + length)
        max_val = max(product, max_val)
    return max_val


def _create_downwards_diagonal(matrix, startrow, startcol):
    indices = zip(range(startrow, matrix.num_rows()), range(startcol, matrix.num_columns()))
    return [matrix[x[0]][x[1]] for x in indices]


def calculate_max_row_product(length, matrix):
    max_val = -1
    for i in xrange(matrix.num_rows()):
        max_val_for_column = _calculate_max_product_for_vector(matrix[i], length)
        max_val = max(max_val, max_val_for_column)
    return max_val


def calculate_max_downward_diagonal(length, matrix):
    max_val = -1
    for i in xrange(matrix.num_rows()):
        max_val_for_downwards_diagonal = _calculate_max_product_for_vector(_create_downwards_diagonal(matrix, i, 0),
                                                                           length)
        max_val = max(max_val, max_val_for_downwards_diagonal)
    for i in xrange(matrix.num_columns()):
        max_val_for_downwards_diagonal = _calculate_max_product_for_vector(_create_downwards_diagonal(matrix, 0, i),
                                                                           length)
        max_val = max(max_val, max_val_for_downwards_diagonal)
    return max_val


def flip_horizontally(matrix):
    m = Matrix(matrix.num_rows(), matrix.num_columns())
    for i in xrange(m.num_rows()):
        for j in xrange(m.num_columns()):
            m[i][j] = matrix[m.num_rows() - i - 1][j]
    return m


def largest_grid_product(matrix, length):
    max_val = max(calculate_max_row_product(length, matrix),
                  calculate_max_row_product(length, matrix.transpose()),
                  calculate_max_downward_diagonal(length, matrix),
                  calculate_max_downward_diagonal(length, flip_horizontally(matrix)))
    return max_val