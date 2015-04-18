#!/usr/bin/python

import operator
import functools

nums = []
with open("../data/p011.txt") as f:
    nums = f.read().strip(' \t\n\r"').split('\n')

for i in range(len(nums)):
    nums[i] = [int(i) for i in nums[i].split(' ')]

max_prod = 0

for y in range(20):
    for x in range(20):
        if x <= 16:
            prod = functools.reduce(operator.mul, nums[y][x:x + 4])
            if prod > max_prod:
                max_prod = prod
        if y <= 16:
            prod = functools.reduce(operator.mul, [nums[y][x], nums[y + 1][x], nums[y + 2][x], nums[y + 3][x]])
            if prod > max_prod:
                max_prod = prod
        if x <= 16 and y <= 16:
            prod = functools.reduce(operator.mul, [
                nums[y][x], nums[y + 1][x + 1], nums[y + 2][x + 2], nums[y + 3][x + 3]])
            if prod > max_prod:
                max_prod = prod
        if x <= 16 and y >= 4:
            prod = functools.reduce(operator.mul, [
                nums[y][x], nums[y - 1][x + 1], nums[y - 2][x + 2], nums[y - 3][x + 3]])
            if prod > max_prod:
                max_prod = prod

print(max_prod)
