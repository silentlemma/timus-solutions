"""One public key from a seed and a mode, made as the statement describes:
an N-bit prime q, an L-bit prime p with q dividing p - 1, g of order q,
y = g^x and an N-bit hash. Mode 1 takes the largest N and L, mode 2 the
largest N with L = N + 3, mode 3 random sizes, mode 4 small sizes."""

import random
import sys

BASES = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)
MOST_N = 36
MOST_L = 60
GAP = 3  # L is at least N + 3


def is_prime(n):
    if n < 2:
        return False
    for b in BASES:
        if n % b == 0:
            return n == b
    d, s = n - 1, 0
    while d % 2 == 0:
        d //= 2
        s += 1
    for a in BASES:
        x = pow(a, d, n)
        if x in (1, n - 1):
            continue
        for _ in range(s - 1):
            x = x * x % n
            if x == n - 1:
                break
        else:
            return False
    return True


def key(rng, n_bits, l_bits):
    while True:
        q = rng.randrange(1 << (n_bits - 1), 1 << n_bits)
        if not is_prime(q):
            continue
        # p = q t + 1 with exactly l_bits bits
        lo = ((1 << (l_bits - 1)) - 1) // q + 1
        hi = ((1 << l_bits) - 2) // q
        for _ in range(1000):
            t = rng.randint(lo, hi)
            p = q * t + 1
            if is_prime(p):
                break
        else:
            continue
        g = 1
        while g == 1:
            g = pow(rng.randrange(2, p - 1), (p - 1) // q, p)
        x = rng.randrange(1, q)
        h = rng.randrange(1 << (n_bits - 1), 1 << n_bits)
        return n_bits, l_bits, q, p, g, pow(g, x, p), h


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n_bits, l_bits = MOST_N, MOST_L
    elif mode == 2:
        n_bits, l_bits = MOST_N, MOST_N + GAP
    elif mode == 3:
        n_bits = rng.randint(3, MOST_N)
        l_bits = rng.randint(n_bits + GAP, MOST_L)
    else:
        n_bits = rng.randint(3, 6)
        l_bits = rng.randint(n_bits + GAP, n_bits + 6)
    print(*key(rng, n_bits, l_bits))


main()
