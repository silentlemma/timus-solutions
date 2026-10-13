"""A picture from a seed and a mode. Mode 1 gives 1000 x 1000
random cells, mode 2 open ground everywhere, mode 3 crosses everywhere,
so no two secrets meet unless they touch, mode 4 a grid of walls with
random holes. Mode 5 gives a 1000 x 1 random column with 100 secrets,
mode 6 a 1000 x 1000 random picture without secrets, and mode 7 closed
rooms of random sizes with 100 secrets at wall intersections. Modes
1, 2, 4 and 7 have 100 secrets; legacy mode 3 has 103."""

import random
import sys

SIDE = 1000
SECRETS = 100
CELL = 10  # the wall grid of mode 4 has rooms of this size
HOLES = 100000


def extra_picture(rng, mode):
    if mode == 5:
        pic = [[rng.choice(".-|+")] for _ in range(SIDE)]
        for r in rng.sample(range(SIDE), SECRETS):
            pic[r][0] = "#"
    elif mode == 6:
        pic = [[rng.choice(".-|+") for _ in range(SIDE)] for _ in range(SIDE)]
    else:
        rows = [0] + sorted(rng.sample(range(1, SIDE - 1), 13)) + [SIDE - 1]
        cols = [0] + sorted(rng.sample(range(1, SIDE - 1), 13)) + [SIDE - 1]
        pic = [["."] * SIDE for _ in range(SIDE)]
        for r in rows:
            pic[r] = ["-"] * SIDE
        for c in cols:
            for r in range(SIDE):
                pic[r][c] = "+" if r in rows else "|"
        for r, c in rng.sample([(r, c) for r in rows for c in cols], SECRETS):
            pic[r][c] = "#"
    return pic


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode in (5, 6, 7):
        pic = extra_picture(rng, mode)
        print("\n".join("".join(row) for row in pic))
        return
    if mode == 1:
        pic = [[rng.choice(".-|+++") for _ in range(SIDE)] for _ in range(SIDE)]
    elif mode == 2:
        pic = [["."] * SIDE for _ in range(SIDE)]
    elif mode == 3:
        pic = [["+"] * SIDE for _ in range(SIDE)]
    else:
        pic = [["."] * SIDE for _ in range(SIDE)]
        for r in range(SIDE):
            for c in range(SIDE):
                if r % CELL == 0 and c % CELL == 0:
                    pic[r][c] = "+"
                elif r % CELL == 0:
                    pic[r][c] = "-"
                elif c % CELL == 0:
                    pic[r][c] = "|"
        for _ in range(HOLES):
            r, c = rng.randrange(SIDE), rng.randrange(SIDE)
            if pic[r][c] != "+":
                pic[r][c] = "."
    for r, c in rng.sample([(r, c) for r in range(0, SIDE, 7) for c in range(0, SIDE, 7)], SECRETS):
        pic[r][c] = "#"
    if mode == 3:
        pic[1][1] = pic[1][2] = pic[2][2] = "#"  # a few that touch
    print("\n".join("".join(row) for row in pic))


main()
