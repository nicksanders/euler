#!/usr/bin/python


def prime_sieve(limit=125000):
    if limit % 2 != 0:
        limit += 1
    sieve = [True] * limit
    sieve[0], sieve[1] = [False] * 2
    for ind, val in enumerate(sieve):
        if val is True:
            sieve[ind * 2::ind] = [False] * (((limit - 1) // ind) - 1)
    return sieve


def primes(limit=125000):
    return [i for i, v in enumerate(prime_sieve(limit)) if v is True]


limit = 1000

for d in primes(limit)[::-1]:
    period = 1
    while pow(10, period, d) != 1:
        period += 1
    if d - 1 == period:
        break

print(d)
