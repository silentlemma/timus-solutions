"""One area K: a seed and a mode.

Mode 1 chooses uniformly from 1..3000, mode 2 from 3001..500000,
and mode 3 from 500001..1000000. All modes use seeded randomness.
"""

import random
import sys

LIMIT = 10**6


def main():
    seed, mode = map(int, sys.argv[1:])
    low, high = {1: (1, 3000), 2: (3001, LIMIT // 2), 3: (LIMIT // 2 + 1, LIMIT)}[mode]
    print(random.Random(seed).randint(low, high))


if __name__ == "__main__":
    main()
