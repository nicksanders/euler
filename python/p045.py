#!/usr/bin/python


def is_triangle(n):
    d = (((1 + 8 * n) ** 0.5) - 1.0) / 2
    return d == int(d)


def is_pentagonal(n):
    d = ((1 + 24 * n) ** 0.5 + 1.0) / 6
    return d == int(d)

i = 143
result = 0

while True:
    i += 1
    a = i * (2 * i - 1)

    if is_pentagonal(a):
        result = a
        break

print(result)
