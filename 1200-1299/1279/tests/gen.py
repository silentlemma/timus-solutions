"""A warehouse: a seed and a mode.

Mode 1: small dimensions and few containers.
Mode 2: up to 100 x 100 sections and K up to 10^7.
Mode 3: equal heights with one tall section.
Mode 4: exactly 100 x 100 random heights and K = 10^7.
Mode 5: exactly 100 x 100 random heights, one container short of level 500.
"""

import random
import sys

SIDE = 100
TOP = 1000
LOT = 10**7


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode in (4, 5):
        n = m = SIDE
        rows = [[rng.randint(1, TOP) for _ in range(m)] for _ in range(n)]
        k = LOT if mode == 4 else sum(max(0, TOP // 2 - h) for row in rows for h in row) - 1
        lines = ["%d %d %d" % (n, m, k)] + [" ".join(map(str, r)) for r in rows]
        sys.stdout.write("\n".join(lines) + "\n")
        return
    side = 5 if mode == 1 else SIDE
    n, m = rng.randint(1, side), rng.randint(1, side)
    k = rng.randint(1, 60) if mode == 1 else rng.randint(1, LOT)
    if mode == 3:
        rows = [[TOP // 2] * m for _ in range(n)]
        rows[rng.randrange(n)][rng.randrange(m)] = TOP
    else:
        rows = [[rng.randint(1, TOP if mode == 2 else 9) for _ in range(m)] for _ in range(n)]
    lines = ["%d %d %d" % (n, m, k)] + [" ".join(map(str, r)) for r in rows]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
