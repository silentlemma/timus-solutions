"""A prime p below 10^9 and a value x from a seed.

Mode 1: x random. Mode 2: x a Fibonacci number modulo p, so the answer is not
empty. Mode 3: a small prime and a random x.
Mode 4: a prime just below 10^9 with p mod 5 = 1 and x in the upper half.
Mode 5: p = 65537, whose p - 1 is a power of two, and a random x.
"""

import random
import sys

TOP = 10 ** 9
SMALL = 60
WITNESSES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)


def is_prime(n):
    if n < 2:
        return False
    for w in WITNESSES:
        if n % w == 0:
            return n == w
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for w in WITNESSES:
        y = pow(w, d, n)
        if y in (1, n - 1):
            continue
        for _ in range(s - 1):
            y = y * y % n
            if y == n - 1:
                break
        else:
            return False
    return True


def fibonacci(k, p):
    # (F(k), F(k + 1)) by doubling
    if k == 0:
        return 0, 1
    a, b = fibonacci(k // 2, p)
    c = a * (2 * b - a) % p
    d = (a * a + b * b) % p
    return (d, (c + d) % p) if k % 2 else (c, d)


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    top = SMALL if mode == 3 else TOP
    if mode == 5:
        p = 65537
    elif mode == 4:
        p = rng.randrange(TOP - 100000, TOP)
        while p % 5 != 1 or not is_prime(p):
            p = rng.randrange(TOP - 100000, TOP)
    else:
        p = rng.randrange(2, top)
        while not is_prime(p):
            p = rng.randrange(2, top)
    if mode == 4:
        x = rng.randrange(p // 2, p)
    else:
        x = fibonacci(rng.randrange(TOP), p)[0] if mode == 2 else rng.randrange(p)
    print(p, x)


main()
