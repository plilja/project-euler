def lattice_paths(rows, columns, sub_result={}):
    if rows == 0 or columns == 0:
        return 1
    if (rows, columns) in sub_result:
        return sub_result[(rows, columns)]
    result = lattice_paths(rows - 1, columns, sub_result) + \
             lattice_paths(rows, columns - 1, sub_result)
    sub_result[(rows, columns)] = result
    return result