import sys


def pentagon_numbers_and_difference():
    #3000 is just a guess it would be too slow to run until pentagon_number(n+1)-pentagon_number(n)>currrent solution :(
    nums = [n * (3 * n - 1) / 2 for n in range(1, 3000)]
    nums_s = set(nums)

    minval = sys.maxint
    res = (0, 0)
    for num2 in nums:
        for num1 in nums:
            if num2 >= num1:
                continue
            if num2 + num1 in nums_s and num1 - num2 in nums_s and num2 - num1 < minval:
                minval = num1 - num2
                res = (num2, num1)
                break
    return res

