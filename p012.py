#!/usr/bin/python

import functools


def factors(n):
    return set(functools.reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

num = 1

while True:
    prod = sum(range(1, num + 1))
    t = factors(prod)
    if len(t) >= 500:
        break
    num += 1

print(prod)
