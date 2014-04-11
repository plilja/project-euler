def _calc_product(series, start_idx, end_idx):
    product = 1
    for digit in series[start_idx:end_idx + 1]:
        product *= int(digit)
    return product


def largest_product_in_series(num_digits, series):
    largest_product = 0
    for i in range(num_digits, len(series) + 1):
        product = _calc_product(series, max(0, i - num_digits), i - 1)
        largest_product = max(largest_product, product)

    return largest_product