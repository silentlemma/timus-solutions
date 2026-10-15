"""One test from a seed and a mode: mode 1 a small board with up to five
colours, mode 2 a 50 x 50 board with five colours, mode 3 a 50 x 50
board with two colours, mode 4 a 50 x 50 board of vertical pairs in
alternating colours, so that every move removes only two balls."""

import random
import sys

SIDE = 50
COLORS = "BGRWY"


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n, m = rng.randint(1, 6), rng.randint(1, 6)
        palette = rng.sample(COLORS, rng.randint(1, 5))
    else:
        n = m = SIDE
        palette = COLORS if mode in (2, 4) else rng.sample(COLORS, 2)
    print(n, m)
    for r in range(n):
        if mode == 4:
            print("".join(palette[(r // 2 + c) % len(palette)] for c in range(m)))
        else:
            print("".join(rng.choice(palette) for _ in range(m)))


main()
