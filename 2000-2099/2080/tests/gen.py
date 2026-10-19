"""Cards and uses from a seed.

Mode 1: a few cards and uses. Mode 2: 10^5 cards and 10^5 random uses.
Mode 3: 10^5 cards, uses among ten of them. Mode 4: every card used once,
in a random order. Mode 5: a single card used 10^5 times.
"""

import random
import sys

SMALL = 8
MAX = 10 ** 5
FEW = 10


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    if mode == 1:
        n, k = rng.randint(1, SMALL), rng.randint(1, SMALL)
        uses = [rng.randint(1, n) for _ in range(k)]
    elif mode == 2:
        n = k = MAX
        uses = [rng.randint(1, n) for _ in range(k)]
    elif mode == 3:
        n = k = MAX
        few = rng.sample(range(1, n + 1), FEW)
        uses = [rng.choice(few) for _ in range(k)]
    elif mode == 4:
        n = k = MAX
        uses = rng.sample(range(1, n + 1), n)
    else:
        n, k = 1, MAX
        uses = [1] * k
    print(n, k)
    print(*uses)


main()
