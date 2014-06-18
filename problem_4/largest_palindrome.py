from common.functions import is_palindrome

def largest_palindrome(number_of_digits_in_product):
    largest_product = pow(10, number_of_digits_in_product) - 1
    smallest_product = pow(10, number_of_digits_in_product - 1)

    _largest_palindrome = -1
    for i in range(largest_product, smallest_product, -1):
        for j in range(i, smallest_product, -1):
            if is_palindrome(i * j):
                _largest_palindrome = max(_largest_palindrome, i * j)
                break
    return _largest_palindrome