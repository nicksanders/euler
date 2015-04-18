#!/usr/bin/python

import time

start = time.time()
total_length = 0

for i in range(1, 1001):
    num = str(i)
    words = []
    nums = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    tens = ['', 'ten', 'twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']
    teens = ['', 'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
    if len(num) == 4:
        words.extend(['one', 'thousand'])
    elif len(num) == 3:
        words.extend([nums[int(num[0])], 'hundred'])
        if num[1] != '0' or num[2] != '0':
            words.append('and')
        num = num[1:]

    if len(num) == 2:
        if num[0] == '1' and num[1] != '0':
            words.append(teens[int(num[1])])
        else:
            if num[0] != '0':
                words.append(tens[int(num[0])])
            num = num[1:]

    if len(num) == 1 and num[0] != '0':
        words.append(nums[int(num[0])])

    total_length += len(''.join(words))

    # print(words)

elapsed = time.time() - start

print("%s found in %s seconds" % (total_length, elapsed))
