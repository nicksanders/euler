#!/usr/bin/python


def is_pentagonal(n):
    d = ((1 + 24 * n) ** 0.5 + 1.0) / 6
    return d == int(d)

i = 0
result = 0
found = False

while not found:
    i += 1
    a = (i * ((3 * i) - 1)) // 2
    for j in range(i - 1, 0, -1):
        b = (j * ((3 * j) - 1)) // 2
        if is_pentagonal(a - b) and is_pentagonal(a + b):
            found = True
            result = a - b
            break

print(result)
