from common.matrix import Matrix


def distinct_powers(n):
    m = Matrix(n + 2, n + 2)

    for i in range(2, n + 1):
        m[i][2] = i ** 2
        for j in range(3, n + 1):
            m[i][j] = m[i][j - 1] * i

    distinct_values = set()
    for i in range(2, n + 1):
        for j in range(2, n + 1):
            distinct_values |= {m[i][j]}

    return len(distinct_values)
