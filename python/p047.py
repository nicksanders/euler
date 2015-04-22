#!/usr/bin/python

from common import prime_sieve, factors


def prime_factors(n, sieve):
    f = factors(n)
    f.remove(1)
    f.remove(n)
    return [i for i in f if sieve[i]]


result = 0
sieve = prime_sieve()

for i in range(647, 1000000):
    found = True
    for j in range(4):
        n = i + j
        pf = prime_factors(n, sieve)
        if len(pf) != 4:
            found = False

    if found is True:
        result = i
        break

print(result)
