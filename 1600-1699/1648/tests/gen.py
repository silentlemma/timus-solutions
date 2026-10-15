"""One test from a seed and a mode: mode 1 a few small months, mode 2
20000 months with large numbers, mode 3 a quiet start and a rush at the
end, which forces long storage."""

import random
import sys

MOST_MONTHS = 20000
MOST = 100000


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n, d = rng.randint(1, 5), rng.randint(1, 3)
        buyers = [rng.randint(0, 4) for _ in range(n)]
    elif mode == 2:
        n, d = MOST_MONTHS, rng.randint(1, MOST)
        buyers = [rng.randint(0, MOST) for _ in range(n)]
    else:
        n, d = MOST_MONTHS, rng.randint(5, 20)
        buyers = [0] * n
        for i in range(n - rng.randint(1, 3), n):
            buyers[i] = MOST
    print(n, d)
    print(*buyers)


main()
