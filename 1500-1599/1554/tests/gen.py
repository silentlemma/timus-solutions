"""One test from a seed and a mode, N = 10000 unless small: mode 1 takes
F = 1 everywhere, mode 2 F(n) = n^k for a random k, mode 3 a random
multiplicative F built from values at prime powers, mode 4 a small N."""

import random
import sys

LARGEST = 10000
SMALL = 30
MOD = 2007


def multiplicative(rng, n):
    f = [0] * (n + 1)
    f[1] = 1
    at_power = {}
    for m in range(2, n + 1):
        # split m into p^e times the rest, with p its smallest prime factor
        p = next(d for d in range(2, m + 1) if m % d == 0)
        power, rest = 1, m
        while rest % p == 0:
            rest //= p
            power *= p
        if rest == 1:
            at_power[m] = rng.randrange(MOD)
            f[m] = at_power[m]
        else:
            f[m] = f[power] * f[rest] % MOD
    return f


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(1, SMALL) if mode == 4 else LARGEST
    if mode == 1:
        f = [0] + [1] * n
    elif mode == 2:
        k = rng.randint(1, 5)
        f = [0] + [pow(i, k, MOD) for i in range(1, n + 1)]
    else:
        f = multiplicative(rng, n)
    print(n)
    print(" ".join(map(str, f[1:])))


main()
