"""20 caps and 100 sets: a seed and a mode. Mode 1 gives random sets and
prices, mode 2 sets of 8 to 12 caps priced by size so that few of them
are worse than another, mode 3 sets of two or three caps, mode 4 random
sets and a random list of wanted caps, mode 5 no sets at all."""

import random
import sys

N = 20
M = 100
TOP = 1000
PER_CAP = 60  # price of a set per cap in mode 2


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    prices = [rng.randint(1, TOP) for _ in range(N)]
    sets = []
    for _ in range(0 if mode == 5 else M):
        if mode == 2:
            size = rng.randint(8, 12)
            cost = min(TOP, PER_CAP * size + rng.randint(-40, 40))
        elif mode == 3:
            size = rng.randint(2, 3)
            cost = rng.randint(1, TOP)
        else:
            size = rng.randint(1, N)
            cost = rng.randint(1, TOP)
        sets.append((cost, rng.sample(range(1, N + 1), size)))
    wanted = list(range(1, N + 1))
    if mode == 4:
        wanted = sorted(rng.sample(wanted, rng.randint(1, N)))
    print(N)
    for p in prices:
        print(p)
    print(len(sets))
    for cost, caps in sets:
        print(cost, len(caps), *caps)
    print(len(wanted), *wanted)


main()
