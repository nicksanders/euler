#!/usr/bin/python


def split_num(n):
    while n > 0:
        x = n % 10
        n = (n - x) // 10
        yield x


def is_palindrome(num):
    return num == num[::-1]


def to_base2(n):
    return str(bin(n))[2:].lstrip('0')


result = []

for n in range(1, 1000000):
    if is_palindrome(to_base2(n)) and is_palindrome(list(split_num(n))):
        result.append(n)

print(result, sum(result))
