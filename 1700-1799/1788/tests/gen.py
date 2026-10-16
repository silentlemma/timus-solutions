"""One test from a seed and a mode: mode 1 any group of up to 100 girls
and 100 boys, mode 2 a small group, mode 3 sensitive girls and calm
boys, so many pairs pay off."""

import random
import sys

LIMIT = 100
UPSET = 1000
SMALL = 6


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    top = SMALL if mode == 2 else LIMIT
    n, m = rng.randint(1, top), rng.randint(1, top)
    if mode == 3:
        girls = [rng.randint(UPSET // 2, UPSET) for _ in range(n)]
        boys = [rng.randint(1, SMALL) for _ in range(m)]
    else:
        girls = [rng.randint(1, UPSET) for _ in range(n)]
        boys = [rng.randint(1, UPSET) for _ in range(m)]
    print(n, m)
    print(*girls)
    print(*boys)


main()
