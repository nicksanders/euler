#!/usr/bin/python

limit = 1000000
cache = {}
cache[1] = 1
result = [1, 1]

for i in range(1, limit):
    n, cnt = i, 0
    while n not in cache:
        if n % 2 == 0:
            n = n // 2
        else:
            n = (3 * n) + 1
        cnt += 1

    tmp = cache[n] + cnt
    cache[i] = tmp
    if tmp > result[1]:
        result = [i, cache[i]]

print(result)
