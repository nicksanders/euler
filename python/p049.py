#!/usr/bin/python

from common import prime_sieve, prime_list, split_num

limit = 10000
result = 0
sieve = prime_sieve(limit=limit)
primes = [i for i in prime_list(sieve=sieve) if i >= 1000]

for i in range(len(primes)):
    for j in range(i + 1, len(primes)):
        a = primes[i]
        b = primes[j]
        diff = b - a
        c = b + diff
        if a == 1487:
            continue
        if c >= limit or sieve[c] is False:
            continue
        a_nums = sorted(split_num(a))
        if a_nums != sorted(split_num(b)):
            continue
        if a_nums != sorted(split_num(c)):
            continue
        result = str(a) + str(b) + str(c)
        print(a, b, c)
        break
    else:
        continue
    break

print(result)
