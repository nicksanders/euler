#!/usr/bin/python


def split_num(n):
    while n > 0:
        x = n % 10
        n = (n - x) // 10
        yield x


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

numerator = 1
denominator = 1

for a in range(10, 100):
    for b in range(a + 1, 100):
        if b % 10 == 0 or a == b:
            continue
        c = a / b
        a2 = list(split_num(a))
        b2 = list(split_num(b))
        if any(i in b2 for i in a2) and not all(i in b2 for i in a2):
            if a2[0] in b2:
                x = a2[0]
            else:
                x = a2[1]
            a2.remove(x)
            b2.remove(x)
            if b2[0] > 0 and a2[0] / b2[0] == c:
                numerator *= a2[0]
                denominator *= b2[0]

g = gcd(numerator, denominator)
print(denominator // g)
