#!/usr/bin/python


def fib(n):
    a, b = 1, 1
    while n > 2:
        a, b = a + b, a
        n -= 1
    return a

for i in range(1, 10000):
    f = fib(i)
    if len(str(f)) == 1000:
        break

print(i)
