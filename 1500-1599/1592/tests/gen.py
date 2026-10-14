"""One test from a seed and a mode: n clocks showing h:mm:ss. Mode 1 is
50000 random clocks, mode 2 50000 clocks within a few minutes of each
other around 12 o'clock, mode 3 50000 clocks on a handful of times, mode 4
a few random clocks."""

import random
import sys

MOST = 50000
CYCLE = 12 * 3600
FEW = 8
NEAR = 600  # seconds either side of 12 o'clock in mode 2


def show(t):
    h, rest = divmod(t, 3600)
    return "%d:%02d:%02d" % (h or 12, rest // 60, rest % 60)


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        times = [rng.randrange(CYCLE) for _ in range(MOST)]
    elif mode == 2:
        times = [rng.randint(-NEAR, NEAR) % CYCLE for _ in range(MOST)]
    elif mode == 3:
        spots = [rng.randrange(CYCLE) for _ in range(FEW)]
        times = [rng.choice(spots) for _ in range(MOST)]
    else:
        times = [rng.randrange(CYCLE) for _ in range(rng.randint(1, FEW))]
    print(len(times))
    for t in times:
        print(show(t))


main()
