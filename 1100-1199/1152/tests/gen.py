"""Monsters on N balconies: a seed, N and a mode. Mode 0 takes random
counts from 1 to 100, mode 1 puts large counts far apart among small
ones, mode 2 makes the counts grow around the circle."""

import random
import sys

TOP = 100
SPREAD = 4


def main():
    seed, n, mode = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    if mode == 1:
        counts = [TOP if i % SPREAD == 0 else rng.randint(1, SPREAD) for i in range(n)]
    elif mode == 2:
        counts = [1 + (TOP - 1) * i // (n - 1) for i in range(n)]
    else:
        counts = [rng.randint(1, TOP) for _ in range(n)]
    sys.stdout.write("%d\n%s\n" % (n, " ".join(map(str, counts))))


if __name__ == "__main__":
    main()
