from common.ulam_spiral import *

def number_spiral_diagonals(n):
    if n == 1:
        return 1
    if n % 2 != 1:
        raise ValueError("Illegal spiral size")
    return sum(sum(corners) for corners in ulam_spiral_corners_upto(n)) - 3