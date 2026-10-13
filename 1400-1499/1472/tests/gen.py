"""One test from seed, mode and optional size (default 100000). Mode 1 picks each
commander at random, mode 2 is one long chain with a private at the end and
prices of at least 500, mode 3 has every soldier report to the general at
the highest price, mode 4 hangs each soldier close below the previous ones
(deep, narrow trees), mode 5 is a random tree where most prices are 0 or
tiny. Mode 6 is a complete binary tree with positive random prices. Mode 7
is a long handle ending in a wide fan of privates. Mode 8 is a two-level
tree with many commanders and competing cuts above and below them. Mode 9
is a random tree with many direct subordinates of the general and no free
links."""

import random
import sys

LARGEST = 100000
HIGHEST = 1000
CLOSE = 5  # in mode 4 the commander is at most this many numbers back
TINY = 3


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    n = int(sys.argv[3]) if len(sys.argv) > 3 else LARGEST
    if not 2 <= n <= LARGEST or not 1 <= mode <= 9:
        raise ValueError("expected 2 <= size <= 100000 and 1 <= mode <= 9")
    rng = random.Random(seed)
    lines = [str(n)]
    handle = max(2, n // 2)
    commanders = max(1, n // 50)
    for i in range(2, n + 1):
        if mode == 2:
            boss = i - 1
        elif mode == 3:
            boss = 1
        elif mode == 4:
            boss = max(1, i - rng.randint(1, CLOSE))
        elif mode == 6:
            boss = i // 2
        elif mode == 7:
            boss = i - 1 if i <= handle else handle
        elif mode == 8:
            boss = 1 if i <= commanders + 1 else rng.randint(2, commanders + 1)
        elif mode == 9:
            boss = 1 if rng.randrange(3) == 0 else rng.randint(1, i - 1)
        else:
            boss = rng.randint(1, i - 1)
        if mode == 3:
            price = HIGHEST
        elif mode == 2:
            price = rng.randint(HIGHEST // 2, HIGHEST)
        elif mode == 5:
            price = rng.randint(0, TINY) if rng.random() < 0.9 else rng.randint(0, HIGHEST)
        elif mode == 7:
            price = HIGHEST if i <= handle else rng.randint(1, HIGHEST)
        elif mode == 8:
            price = rng.randint(HIGHEST // 2, HIGHEST) if boss == 1 else rng.randint(0, 40)
        elif mode in (6, 9):
            price = rng.randint(1, HIGHEST)
        else:
            price = rng.randint(0, HIGHEST)
        lines.append("%d %d" % (boss, price))
    print("\n".join(lines))


main()
