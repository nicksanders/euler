#!/usr/bin/python


def split_num(n):
    while n > 0:
        x = n % 10
        n = (n - x) // 10
        yield x


def join_nums(nums):
    r = 0
    m = 1
    for n in nums[::-1]:
        r += n * m
        m *= 10
    return r


def permutations(l):
    if len(l) <= 1:
        yield l
    else:
        for i in range(len(l)):
            for p in permutations(l[:i] + l[i + 1:]):
                yield l[i:i + 1] + p

result = set()

for a in range(2, 100):
    b_start = 123 if a > 9 else 1234
    b_end = 10000 // a + 1
    for b in range(b_start, b_end):
        c = a * b
        nums = set(list(split_num(a)) + list(split_num(b)) + list(split_num(c)))
        if not nums ^ {1, 2, 3, 4, 5, 6, 7, 8, 9}:
            result.add(c)


print(sum(result))
