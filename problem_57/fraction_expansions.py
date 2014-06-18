from common.decorators import listify


@listify
def fraction_expansions(iterations):
    num, den = 1, 1
    for i in range(0, iterations):
        num += den
        num, den = den, num
        num += den
        yield (num, den)