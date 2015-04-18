#!/usr/bin/python

import operator
import functools

with open("../data/p008.txt") as f:
    num = f.read().replace('\n', '')

max_prod = 0

for i in range(0, len(num) - 12):
    prod = functools.reduce(operator.mul, [int(x) for x in num[i:i + 13]], 1)
    if prod > max_prod:
        max_prod = prod

print(max_prod)
