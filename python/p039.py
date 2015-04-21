#!/usr/bin/python


def get_value(item):
    return item[1]


result = {}

for a in range(1, 100000):
    for b in range(a, 100000):
        p = a + b + ((a * a) + (b * b)) ** 0.5
        if p == int(p):
            if p in result:
                result[p] += 1
            else:
                result[p] = 1


print(sorted(result.items(), key=get_value, reverse=True)[0])
