"""Three lists of own numbers from a seed and a mode: mode 1 short lists
of small numbers, 2 the longest lists of numbers up to 10^9, 3 the
longest lists drawn from a small pool so that many numbers are shared,
4 the longest lists that share nothing, 5 three equal longest lists."""

import random
import sys

PLAYERS = 3
LONGEST = 4000
LARGEST = 10 ** 9
FEW = 8
POOL = 6000


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    lists = []
    shared = rng.sample(range(1, LARGEST + 1), LONGEST)
    for p in range(PLAYERS):
        if mode == 1:
            own = rng.sample(range(1, FEW * 2), rng.randint(1, FEW))
        elif mode == 2:
            own = rng.sample(range(1, LARGEST + 1), LONGEST)
        elif mode == 3:
            own = rng.sample(range(1, POOL + 1), LONGEST)
        elif mode == 4:
            own = [PLAYERS * rng.randint(0, LARGEST // PLAYERS - 1) + p + 1 for _ in range(LONGEST)]
            own = list(set(own))
        else:
            own = shared
        lists.append(sorted(own))
    for own in lists:
        print(len(own))
        print(*own)


main()
