"""Up to 100 tests: a seed and a mode. Mode 1 draws a, b and k at random,
mode 2 uses the primes just below 10000 as b, where periods can be almost
b digits long, mode 3 makes many a / b whole or finite.
Mode 4 uses base 2 and twice a large odd prime: a one-digit prefix followed
by a long period. Mode 5 prints random pairs of equivalent fractions with
different common factors in their input numerator and denominator.
"""

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
    if mode == 4:
        primes = [p for p in range(4500, 5000) if all(p % d for d in range(2, int(p**0.5) + 1))]
        for _ in range(TESTS):
            p = rng.choice(primes)
            a = 2 * rng.randrange(TOP // 2) + 1
            while a % p == 0:
                a = 2 * rng.randrange(TOP // 2) + 1
            lines.append("%d %d 2" % (a, 2 * p))
        print("\n".join(lines + ["0 0"]))
        return
    if mode == 5:
        for _ in range(TESTS // 2):
            a, b = rng.randint(1, 100), rng.randint(2, 100)
            k = rng.randint(2, LARGEST_BASE)
            factors = rng.sample(range(2, TOP // max(a, b) + 1), 2)
            for factor in factors:
                lines.append("%d %d %d" % (a * factor, b * factor, k))
        print("\n".join(lines + ["0 0"]))
        return
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
