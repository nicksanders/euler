#!/usr/bin/python

from common import prime_sieve, prime_list

limit = 1000000
sieve = prime_sieve(limit)
primes = prime_list(sieve=sieve)
c_primes = [primes[0]]

for i in range(1, len(primes)):
    v = c_primes[i - 1] + primes[i]
    if v > limit * 2:
        break
    c_primes.append(v)

terms = 1
max_prime = 2

for i in range(len(c_primes)):
    for j in range(i + terms, len(c_primes)):
        n = c_primes[j] - c_primes[i]
        if j - i > terms and n < limit and sieve[n]:
            terms = j - i
            max_prime = n


print(terms, max_prime)
