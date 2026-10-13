"""A 1000 x 1000 picture with 100 secrets: a seed and a mode. Mode 1 gives
random cells, mode 2 open ground everywhere, mode 3 crosses everywhere,
so no two secrets meet unless they touch, mode 4 a grid of walls with
random holes."""

import random
import sys

SIDE = 1000
SECRETS = 100
CELL = 10  # the wall grid of mode 4 has rooms of this size
HOLES = 100000


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
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
