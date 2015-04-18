#!/usr/bin/python


def calc_sum_at_row(nums, row_num):
    for i in range(len(nums[row_num])):
        nums[row_num][i] += max([nums[row_num + 1][i], nums[row_num + 1][i + 1]])

    if len(nums[row_num]) == 1:
        return nums[row_num][0]
    else:
        return calc_sum_at_row(nums, row_num - 1)


nums = []
with open("../data/p018.txt") as f:
    nums = f.read().strip(' \t\n\r"').split('\n')

for i in range(len(nums)):
    nums[i] = [int(i) for i in nums[i].split(' ')]

print(calc_sum_at_row(nums, len(nums) - 2))
