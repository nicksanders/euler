#!/usr/bin/python

total = 0
week_days = [0, 1, 2, 3, 4, 5, 6, 0, 1, 2, 3, 4, 5, 6]
months_norm = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
months_leap = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
start_day = 2

for year in range(1901, 2001):
    months = months_norm
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        months = months_leap

    for month in months:
        if start_day == 0:
            total += 1
        start_day = week_days[(month % 7) + start_day]

print(total)
