"""One test from a seed and a mode: mode 1 capacities up to 10, mode 2
capacities up to 10^9, mode 3 a mix of tiny and huge capacities."""

import random
import sys

BRIDGES = 6
FEW = 10
MOST = 10**9


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        caps = [rng.randint(1, FEW) for _ in range(BRIDGES)]
    elif mode == 2:
        caps = [rng.randint(1, MOST) for _ in range(BRIDGES)]
    else:
        caps = [rng.choice((rng.randint(1, FEW), rng.randint(MOST - FEW, MOST)))
                for _ in range(BRIDGES)]
    print(*caps)


main()
