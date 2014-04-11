def fibonacci_with_digits(num_digits):
    if num_digits == 1:
        return 1
    n = 3
    fib = 2
    (fa, fb) = (1, 2)
    while len(str(fib)) < num_digits:
        fib = fa + fb
        (fa, fb) = (fb, fib)
        n += 1
    return n
