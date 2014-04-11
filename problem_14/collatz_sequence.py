cached_results = {}


def collatz_seq_len(input_n):
    count = 0
    n = input_n
    while n != 1:
        if n in cached_results:
            result = count + cached_results[n]
            cached_results[input_n] = result
            return result
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        count += 1
    cached_results[input_n] = count + 1
    return cached_results[input_n]


def longest_collatz_seq(less_than_number):
    res = -1
    highest = -1
    for i in range(1, less_than_number):
        seq_len_for_i = collatz_seq_len(i)
        if seq_len_for_i > highest:
            res = i
            highest = seq_len_for_i

    return res