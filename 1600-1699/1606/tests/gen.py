"""One test from a seed and a mode: flags with distinct x and distinct y
from 1 to 99999. Mode 1 is 50000 random flags, mode 2 a perfect zigzag,
mode 3 x growing all the way down, mode 4 long runs in each direction,
mode 5 a few flags, mode 6 a maximal zigzag with the last turn removed,
mode 7 a maximal collinear middle run with a turn at either end."""

import random
import sys

MOST = 50000
TOP = 99999
FEW = 8


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(1, FEW) if mode == 5 else MOST
    ys = rng.sample(range(1, TOP + 1), n)
    ys.sort(reverse=True)
    xs = rng.sample(range(1, TOP + 1), n)
    if mode == 2:
        xs.sort()
        half = (n + 1) // 2
        low, high = xs[:half], xs[half:][::-1]
        xs = [low[i // 2] if i % 2 == 0 else high[i // 2] for i in range(n)]
    elif mode == 3:
        xs.sort()
    elif mode == 4:
        xs.sort()
        runs, i = [], 0
        while i < n:
            length = rng.randint(1, 500)
            runs.append(xs[i : i + length] if len(runs) % 2 == 0 else xs[i : i + length][::-1])
            i += length
        xs = [x for run in runs for x in run]
    elif mode == 6:
        ys = [TOP - 2 * i for i in range(n)]
        xs = [i // 2 + 1 if i % 2 == 0 else TOP - i // 2 for i in range(n)]
        xs[-2:] = xs[-2:][::-1]
    elif mode == 7:
        ys = [TOP - 2 * i for i in range(n)]
        xs = [1] + list(range(n, 2, -1)) + [TOP]
    flags = list(zip(xs, ys))
    rng.shuffle(flags)
    print(n)
    for x, y in flags:
        print(x, y)


main()
