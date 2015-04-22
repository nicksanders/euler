
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


def prime_list(limit=125000, sieve=None):
    if sieve is None:
        sieve = prime_sieve(limit)
    return [i for i, v in enumerate(sieve) if v is True]


def permutations(l):
    if len(l) <= 1:
        yield l
    else:
        for i in range(len(l)):
            for p in permutations(l[:i] + l[i + 1:]):
                yield l[i:i + 1] + p


def proper_divisors(n):
    d = {1}
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            d |= {i, n // i}
    return d
