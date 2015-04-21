#!/usr/bin/python

from common import split_num, join_nums


result = 0

for i in range(2, 10000):
    nums = []
    for n in range(1, 10):
        nums.extend(split_num(i * n))

        if n > 1 and len(nums) == 9 and not set(nums) ^ {1, 2, 3, 4, 5, 6, 7, 8, 9}:
            if join_nums(nums) > result:
                result = join_nums(nums)

        if len(nums) > 9:
            break

print(result)
