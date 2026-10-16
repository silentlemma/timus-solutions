"""One test from a seed and a mode: mode 1 up to 6 mages with short stays,
mode 2 100 mages with random arrivals and stays, mode 3 100 mages all
staying the same minutes, with k set right at or just under what they
need, mode 4 100 mages with long stays and k = 1."""

import random
import sys

FEW = 6
MOST = 100
LATEST = 1000
SHORT = 6
TIGHT = 40


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n, k = rng.randint(1, FEW), rng.randint(1, 3)
        mages = [(rng.randint(0, SHORT), rng.randint(2, SHORT)) for _ in range(n)]
    elif mode == 2:
        n, k = MOST, rng.randint(1, 5)
        mages = [(rng.randint(0, TIGHT), rng.randint(2, TIGHT)) for _ in range(n)]
    elif mode == 3:
        n = MOST
        stay = rng.randint(2, TIGHT)
        k = -(-2 * n // stay) - rng.randint(0, 1)
        t = rng.randint(0, LATEST)
        mages = [(t, stay)] * n
    else:
        n, k = MOST, 1
        mages = [(rng.randint(0, LATEST), rng.randint(2, LATEST)) for _ in range(n)]
    print(n, max(1, k))
    for t, s in mages:
        print(t, s)


main()
