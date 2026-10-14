"""One test from a seed and a mode. Mode 1 is the largest size with mixed
queries and P near 10^9, mode 2 the same with the smallest prime P, mode 3
is small, mode 4 asks only K = 4 over long intervals, mode 5 mostly
updates."""

import random
import sys

SIZE = 80000
QUERIES = 100000
SMALL = 12
VALUE = 100000
MOST = 4
PRIMES = {1: 999999937, 2: 1009, 3: 1013, 4: 999999929, 5: 998244353}


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(1, SMALL) if mode == 3 else SIZE
    m = rng.randint(1, SMALL) if mode == 3 else QUERIES
    p = PRIMES[mode]
    lines = ["%d %d %d" % (n, m, p)]
    lines.append(" ".join(str(rng.randint(-VALUE, VALUE)) for _ in range(n)))
    share = 0.9 if mode == 5 else 0.5
    for _ in range(m):
        if mode != 4 and rng.random() < share:
            lines.append("I %d %d" % (rng.randint(1, n), rng.randint(-VALUE, VALUE)))
            continue
        if mode == 4:
            left = rng.randint(1, n // 10)
            right = rng.randint(n - n // 10, n)
        else:
            left = rng.randint(1, n)
            right = rng.randint(left, n)
        k = rng.randint(1, min(MOST, right - left + 1))
        lines.append("C %d %d %d" % (left, right, MOST if mode == 4 else k))
    print("\n".join(lines))


main()
