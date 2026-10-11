"""A position: a seed, N and a mode. Mode 1 places the three pieces
anywhere legal, mode 2 puts the white pawn on its starting row, mode 3
keeps the king far from the white pawn, mode 4 puts the black pawn one
step from promotion."""

import random
import sys


def square(x, y):
    return "%s%d" % (chr(ord("a") + x), y + 1)


def main():
    seed, n, mode = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    while True:
        wx, wy = rng.randrange(n), rng.randint(1, n - 2)
        bx, by = rng.randrange(n), rng.randint(1, n - 2)
        kx, ky = rng.randrange(n), rng.randrange(n)
        if mode == 2:
            wy = 1
        if mode == 4:
            by = 1
        if mode == 3 and max(abs(kx - wx), abs(ky - wy)) < n // 2:
            continue
        cells = {(wx, wy), (bx, by), (kx, ky)}
        checked = ky == wy + 1 and abs(kx - wx) == 1
        if len(cells) == 3 and not checked:
            break
    print(n)
    print(square(wx, wy), square(bx, by), square(kx, ky))


if __name__ == "__main__":
    main()
