def double_palindromes(less_than):
    for i in range(1, less_than):
        if _is_palindrome(str(i)) and _is_palindrome(_binary(i)):
            yield i


def _is_palindrome(string):
    return string == string[::-1]


def _binary(decimal_number):
    return bin(decimal_number)[2:]
