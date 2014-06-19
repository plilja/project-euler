import itertools


def ulam_spiral_corners():
    corners_at_level = (1, 1, 1, 1)
    level = 1
    while True:
        yield corners_at_level
        (tr, tl, bl, br) = corners_at_level
        corners_at_level = (br + level + 1, br + 2 * (level + 1), br + 3 * (level + 1), br + 4 * (level + 1))
        level += 2


def ulam_spiral_corners_upto(n):
    assert n % 2 == 1
    return itertools.islice(ulam_spiral_corners(), n / 2 + 1)

def ulam_spiral_corners_except_center():
    res = ulam_spiral_corners()
    res.next()
    return res