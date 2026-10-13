"""Generate positions: seed, mode, N (1 <= N <= 1000).

Mode 1: random positions from 0 to 9, with many duplicates.
Mode 2: random positions from 999990 to 1000000, near the upper bound.
"""

import random
import sys

MAX_POSITION = 10**6


def main():
    sys.stdout.reconfigure(newline="\n")
    seed, mode, n = map(int, sys.argv[1:])
    if mode not in (1, 2) or not 1 <= n <= 1000:
        raise ValueError("expected mode 1 or 2 and 1 <= N <= 1000")
    rng = random.Random(seed)
    if mode == 1:
        positions = [rng.randint(0, 9) for _ in range(n)]
    else:
        positions = [MAX_POSITION - rng.randint(0, 10) for _ in range(n)]
    print(n)
    print(*positions)


if __name__ == "__main__":
    main()
