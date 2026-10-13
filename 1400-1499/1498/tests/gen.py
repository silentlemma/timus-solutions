"""One test from a seed and a mode: mode 1 is a random field up to
100 x 100 with up to 1000 steps, mode 2 gives few steps, mode 3 puts the
demon in a corner, mode 4 is a narrow strip."""

import random
import sys

LARGEST = 100
STEPS = 1000
FEW = 10


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    n, m = rng.randint(1, LARGEST), rng.randint(1, LARGEST)
    if mode == 4:
        n = 1
    if n * m < 2:
        m = 2
    steps = rng.randint(1, FEW if mode == 2 else STEPS)
    while True:
        knight = (rng.randint(1, n), rng.randint(1, m))
        demon = (
            (rng.choice([1, n]), rng.choice([1, m]))
            if mode == 3
            else (rng.randint(1, n), rng.randint(1, m))
        )
        if knight != demon:
            break
    print(n, m, steps)
    print(*knight)
    print(*demon)


main()
