def maximum_path_sum(triangle):
    copied_triangle = list(triangle)
    for i in range(1, len(copied_triangle)):
        row = copied_triangle[i]
        prev_row = copied_triangle[i - 1]
        for j in xrange(len(row)):
            row[j] += max(prev_row[max(j - 1, 0)], prev_row[min(j, len(prev_row) - 1)])
    return max(copied_triangle[-1])