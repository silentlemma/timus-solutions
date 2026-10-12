"""A room, a number of bounces and two points: a seed and a mode. Mode 1
gives a random room up to 1000 by 1000, mode 2 a small room where many
lines cross the target before the last bounce, mode 3 a long narrow
room, mode 4 the target in the thrower's place."""

import random
import sys

TOP = 1000
MOST = 10


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 2:
        w, h = rng.randint(2, 6), rng.randint(2, 6)
    elif mode == 3:
        w, h = TOP, rng.randint(2, 5)
    else:
        w, h = rng.randint(2, TOP), rng.randint(2, TOP)
    n = rng.randint(1, MOST)
    ax, ay = rng.randint(1, w - 1), rng.randint(1, h - 1)
    bx, by = rng.randint(1, w - 1), rng.randint(1, h - 1)
    if mode == 4:
        bx, by = ax, ay
    print(w, h)
    print(n)
    print(ax, ay, bx, by)


main()
