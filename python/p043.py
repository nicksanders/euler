#!/usr/bin/python

from common import permutations, join_nums

result = 0
nums = list(range(10))
primes = [0, 2, 3, 5, 7, 11, 13, 17]

for p in permutations(nums):
    all_div = True
    for i, n in enumerate(primes):
        if i < 1:
            continue
        if join_nums(p[i:i + 3]) % n != 0:
            all_div = False

    if all_div:
        result += join_nums(p)

print(result)
