"""One test from a seed and a mode: mode 1 counts from 1 to 1000, mode 2
counts from 1 to 3, mode 3 counts of 1 and 1000 only, mode 4 one cell
of 1000 among ones."""

import random
import sys

SIDE = 8
MOST = 1000
FEW = 3


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    cells = SIDE * SIDE
    if mode == 1:
        v = [rng.randint(1, MOST) for _ in range(cells)]
    elif mode == 2:
        v = [rng.randint(1, FEW) for _ in range(cells)]
    elif mode == 3:
        v = [rng.choice((1, MOST)) for _ in range(cells)]
    else:
        v = [1] * cells
        v[rng.randrange(cells)] = MOST
    for r in range(SIDE):
        print(*v[r * SIDE:(r + 1) * SIDE])


main()
