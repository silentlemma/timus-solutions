"""Carriages and a locomotive: a seed and a mode. Mode 1 draws any of the
four kinds, mode 2 mostly AA and BB with few switching carriages, mode 3
N = 40 and K near N."""

import random
import sys

KINDS = ["AA", "AB", "BA", "BB"]
CARS = 40


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    n = CARS if mode == 3 else rng.randint(1, CARS)
    k = rng.randint(max(1, n - 3), n) if mode == 3 else rng.randint(1, n)
    weights = [4, 1, 1, 4] if mode == 2 else [1, 1, 1, 1]
    cars = rng.choices(KINDS, weights, k=n)
    loco = rng.choice(KINDS)
    sys.stdout.write("%d %d\n%s\n%s\n" % (n, k, loco, "\n".join(cars)))


if __name__ == "__main__":
    main()
