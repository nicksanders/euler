#!/usr/bin/python

sum_of_squares = sum([i * i for i in range(1, 101)])

square_of_sum = sum(range(1, 101))
square_of_sum *= square_of_sum

print(square_of_sum - sum_of_squares)
