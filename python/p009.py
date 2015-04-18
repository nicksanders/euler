#!/usr/bin/python

prod = 0

for c in range(333, 999):
    for b in range(c, 1, -1):
        a = 1000 - b - c
        if (a * a) + (b * b) == c * c:
            prod = a * b * c
            break
    else:
        continue
    break

print(prod)
