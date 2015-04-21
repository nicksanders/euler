#!/usr/bin/python

from common import prime_list, prime_sieve

i = 33
result = 0

sieve = prime_sieve()
primes = prime_list()

while True:
    i += 2
    found = False
    if sieve[i] is True:
        continue
    for p in primes:
        if p > i:
            break
        for s in range(1, 100):
            n = p + (2 * s * s)
            if n > i:
                break
            elif i == n:
                found = True
                break

    if found is False:
        result = i
        break

print(result)
