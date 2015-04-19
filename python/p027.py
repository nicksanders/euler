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


result = [0, 0, 0]
sieve = prime_sieve()

for a in range(-999, 1000):
    for b in range(-999, 1000):
        n = 0
        while True:
            p = abs((n * n) + (a * n) + b)
            if not sieve[p]:
                break
            if n > result[0]:
                result = [n, a, b]
                print(result)
            n += 1

print(result, result[1] * result[2])
