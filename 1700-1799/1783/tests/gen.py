"""One test from a seed and a mode: mode 1 a few months with small
plans, mode 2 10 000 months looking 50 ahead with any plans, mode 3
plans that rise and fall in long waves, mode 4 plans of zero but for
rare spikes, mode 5 all-zero plans at both size limits, mode 6 a bounded
random walk starting at the largest plan (also at both size limits)."""

import math
import random
import sys

FEW = 8
SMALL = 10
MONTHS = 10000
AHEAD = 50
MOST = 100000
WAVE = 300
RARE = 0.01


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n, m = rng.randint(1, FEW), rng.randint(1, FEW)
        plan = [rng.randint(0, SMALL) for _ in range(n + m - 1)]
    else:
        n, m = MONTHS, AHEAD
        count = n + m - 1
        if mode == 2:
            plan = [rng.randint(0, MOST) for _ in range(count)]
        elif mode == 3:
            plan = [int(MOST / 2 * (1 + math.sin(i / WAVE))) for i in range(count)]
        elif mode == 5:
            plan = [0] * count
        elif mode == 6:
            value = MOST
            plan = []
            for _ in range(count):
                plan.append(value)
                value = max(0, min(MOST, value + rng.randint(-1000, 1000)))
        else:
            plan = [MOST if rng.random() < RARE else 0 for _ in range(count)]
    print(n, m)
    print(*plan)


main()
