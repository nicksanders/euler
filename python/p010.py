#!/usr/bin/python


def sum_primes_below_n(n):
    primes = [True] * n
    primes[0], primes[1] = [None] * 2
    prod = 0
    for ind, val in enumerate(primes):
        if val is True:
            primes[ind * 2::ind] = [False] * (((n - 1) // ind) - 1)
            prod += ind
    return prod


print(sum_primes_below_n(2000000))
