"""One test from a seed and a mode: mode 1 a few teams on a small grid of
values, often repeated, mode 2 1500 teams with all values distinct, mode
3 1500 teams on a 40 x 40 grid of values, mode 4 1500 teams with negative
satisfaction except two."""

import random
import sys

MOST = 1500
AGE_LOW = 4 * 10 ** 8
LIMIT = 10 ** 9
GRID = 40


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(2, 8) if mode == 1 else MOST
    teams = []
    for i in range(n):
        if mode == 1:
            a = AGE_LOW + rng.randint(0, 3)
            f = rng.randint(0, 3)
            s = rng.randint(-10, 10)
        elif mode == 3:
            a = AGE_LOW + rng.randint(0, GRID) * 10 ** 7
            f = rng.randint(0, GRID)
            s = rng.randint(-LIMIT, LIMIT)
        else:
            a = rng.randint(AGE_LOW, LIMIT)
            f = rng.randint(0, LIMIT)
            s = rng.randint(-LIMIT, LIMIT)
            if mode == 4:
                s = -abs(s) if i >= 2 else abs(s) // 2
        teams.append((a, f, s))
    print(n)
    for team in teams:
        print(*team)


main()
