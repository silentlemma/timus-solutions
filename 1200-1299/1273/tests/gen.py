"""Sleepers: a seed and a mode. Mode 1 draws up to 100 sleepers with
distinct ends from -1000 to 1000, mode 2 nearly straight sleepers with a
few swaps, mode 3 up to 12 sleepers in a narrow range (many crossings)."""

import random
import sys

TOP = 1000
COUNT = 100


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    k = rng.randint(0, 12) if mode == 3 else rng.randint(1, COUNT)
    span = 20 if mode == 3 else TOP
    left = rng.sample(range(-span, span + 1), k)
    right = rng.sample(range(-span, span + 1), k)
    if mode == 2:
        left.sort()
        right.sort()
        for _ in range(rng.randint(0, 10)):
            i, j = rng.randrange(k), rng.randrange(k)
            right[i], right[j] = right[j], right[i]
    lines = ["%d" % k] + ["%d %d" % p for p in zip(left, right)]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
