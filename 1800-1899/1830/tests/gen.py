"""One pair of page sets from a seed and a mode: mode 1 a few random
pages, mode 2 fifty random pages, mode 3 fifty pages differing only in
the last few."""

import random
import sys

LIMIT = 50
SMALL = 8
TAIL = 4


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(1, SMALL) if mode == 1 else LIMIT
    start = [rng.choice("01") for _ in range(n)]
    goal = [rng.choice("01") for _ in range(n)]
    if mode == 3:
        goal = start[:n - TAIL] + goal[n - TAIL:]
    print(n)
    print("".join(start))
    print("".join(goal))


main()
