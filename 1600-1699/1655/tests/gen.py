"""One test from a seed and a mode: mode 1 a few ships, mode 2 500 ships
with generous distances, mode 3 500 ships that are barely reachable in
time, mode 4 ships straight ahead of the gun among others."""

import random
import sys

MOST = 500
FULL = 360000  # thousandths of a degree


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(1, 6) if mode == 1 else MOST
    a = rng.randrange(FULL)
    w = rng.randint(10, 1000)  # thousandths of a turn a minute
    azimuths = rng.sample(range(FULL), n)
    if mode == 4:
        azimuths[0] = a
    print("%.3f %.3f %d" % (a / 1000, w / 1000, n))
    for b in azimuths:
        if mode == 3:
            d = rng.randint(50000, 200000)
            v = rng.randint(5000, 100000)
        else:
            d = rng.randint(1000, 1000000)
            v = rng.randint(10, 100000)
        print("%.3f %.3f %.3f" % (b / 1000, d / 1000, v / 1000))


main()
