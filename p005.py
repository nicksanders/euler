#!/usr/bin/python

num = 2520

while True:
    success = True
    for i in range(11, 21):
        if num % i != 0:
            success = False
            break

    if success:
        break

    num += 2520


print(num)
