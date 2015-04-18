#!/usr/bin/python

max_product = 0

for i in range(100, 1000):
    for j in range(100, i):
        product = i * j
        if str(product) == str(product)[::-1]:
            if product > max_product:
                max_product = product

print(max_product)
