"""Up to 100 tests: a seed and a mode. Mode 1 draws a, b and k at random,
mode 2 uses the primes just below 10000 as b, where periods can be almost
b digits long, mode 3 makes many a / b whole or finite."""

import random
import sys

TESTS = 100
TOP = 10000
LARGEST_BASE = 36


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    primes = [p for p in range(TOP - 200, TOP) if all(p % d for d in range(2, int(p**0.5) + 1))]
    lines = []
    for _ in range(TESTS):
        k = rng.randint(2, LARGEST_BASE)
        if mode == 1:
            a, b = rng.randint(1, TOP), rng.randint(1, TOP)
        elif mode == 2:
            b = rng.choice(primes)
            a = rng.randint(1, TOP)
        else:
            b = rng.choice([1, 2, 4, 5, 8, 16, k, k * k, 2 * k])
            b = min(b, TOP)
            a = rng.randint(1, TOP)
        lines.append("%d %d %d" % (a, b, k))
    lines.append("0 0")
    print("\n".join(lines))


main()
