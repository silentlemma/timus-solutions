"""One test of 100000 soldiers from a seed and a mode. Mode 1 picks each
commander at random, mode 2 is one long chain with a private at the end and
prices of at least 500, mode 3 has every soldier report to the general at
the highest price, mode 4 hangs each soldier close below the previous ones
(deep, narrow trees), mode 5 is a random tree where most prices are 0 or
tiny."""

import random
import sys

LARGEST = 100000
HIGHEST = 1000
CLOSE = 5  # in mode 4 the commander is at most this many numbers back
TINY = 3


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    lines = [str(LARGEST)]
    for i in range(2, LARGEST + 1):
        if mode == 2:
            boss = i - 1
        elif mode == 3:
            boss = 1
        elif mode == 4:
            boss = max(1, i - rng.randint(1, CLOSE))
        else:
            boss = rng.randint(1, i - 1)
        if mode == 3:
            price = HIGHEST
        elif mode == 2:
            price = rng.randint(HIGHEST // 2, HIGHEST)
        elif mode == 5:
            price = rng.randint(0, TINY) if rng.random() < 0.9 else rng.randint(0, HIGHEST)
        else:
            price = rng.randint(0, HIGHEST)
        lines.append("%d %d" % (boss, price))
    print("\n".join(lines))


main()
