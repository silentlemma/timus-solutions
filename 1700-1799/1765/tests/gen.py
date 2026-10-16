"""One test from a seed and a mode: n is a product of powers of at most
two primes; mode 1 n up to 60, mode 2 n up to 20 000 with a few broken
blades, mode 3 the same with many broken blades, mode 4 a power of one
prime up to 20 000, mode 5 n = 20 000 with only one surviving blade,
mode 6 n = 16 384 with a random half of the blades broken."""

import random
import sys

SMALL = 60
MOST = 20000
FEW = 5


def primes_of(n):
    found, d = set(), 2
    while d * d <= n:
        while n % d == 0:
            found.add(d)
            n //= d
        d += 1
    if n > 1:
        found.add(n)
    return found


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode in (5, 6):
        n = MOST if mode == 5 else 16384
        if mode == 5:
            survivor = rng.randint(1, n)
            broken = [v for v in range(1, n + 1) if v != survivor]
        else:
            broken = sorted(rng.sample(range(1, n + 1), n // 2))
        print(n, len(broken))
        print(*broken)
        return
    top = SMALL if mode == 1 else MOST
    wanted = 1 if mode == 4 else 2
    while True:
        n = rng.randint(max(3, top // 2), top)
        if len(primes_of(n)) == wanted or (mode == 1 and len(primes_of(n)) == 1):
            break
    k = rng.randint(1, FEW) if mode in (2, 4) else rng.randint(1, n - 1)
    broken = sorted(rng.sample(range(1, n + 1), k))
    print(n, k)
    print(*broken)


main()
