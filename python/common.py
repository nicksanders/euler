
def factors(n):
    f = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            f.update([i, n // i])
    return f


def factorial(n):
    f = 1
    for x in range(1, n + 1):
        f *= x
    return f


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def split_num(n):
    nums = []
    while n > 0:
        x = n % 10
        n = n // 10
        nums.append(x)
    return nums[::-1]


def join_nums(nums):
    r = 0
    m = 1
    for n in nums[::-1]:
        r += n * m
        m *= 10
    return r


def prime_sieve(limit=125000):
    if limit % 2 != 0:
        limit += 1
    sieve = [True] * limit
    sieve[0], sieve[1] = [False] * 2
    for ind, val in enumerate(sieve):
        if val is True:
            sieve[ind * 2::ind] = [False] * (((limit - 1) // ind) - 1)
    return sieve


def prime_list(limit=125000):
    return [i for i, v in enumerate(prime_sieve(limit)) if v is True]
