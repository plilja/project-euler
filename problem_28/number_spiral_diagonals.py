def number_spiral_diagonals(n):
    if n == 1:
        return 1
    if n % 2 != 1:
        raise ValueError("Illegal spiral size")

    corners_at_levels = [(3, 5, 7, 9)]
    for i in range(5, n + 1, 2):
        (br, bl, tl, tr) = corners_at_levels[-1]
        corners_at_levels += [(tr + i - 1, tr + 2 * (i - 1), tr + 3 * (i - 1), tr + 4 * (i - 1))]

    return sum([sum(corners_at_level) for corners_at_level in corners_at_levels]) + 1
