#!/usr/bin/python


def split_num(n):
    while n > 0:
        x = n % 10
        n = (n - x) // 10
        yield x


def factorial(n):
    f = 1
    for x in range(1, n + 1):
        f *= x
    return f

result = 0
cache = [factorial(x) for x in range(10)]

for a in range(3, 2540160):
    if a == sum([cache[n] for n in split_num(a)]):
        result += a

print(result)
