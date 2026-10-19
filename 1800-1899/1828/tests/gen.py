"""One sequence from a seed and a mode: mode 1 a short random one, mode
2 the longest random one, mode 3 the longest one close to a steep line,
mode 4 the longest one swinging between the extremes."""

import random
import sys

LIMIT = 10000
SMALL = 20


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(2, SMALL) if mode == 1 else LIMIT
    if mode == 3:
        a = [max(-LIMIT, min(LIMIT, 2 * i - LIMIT + rng.randint(-5, 5))) for i in range(n)]
    elif mode == 4:
        a = [LIMIT if (i // rng.randint(1, 3)) % 2 else -LIMIT for i in range(n)]
    else:
        a = [rng.randint(-LIMIT, LIMIT) for _ in range(n)]
    print(n)
    print(*a)


main()
