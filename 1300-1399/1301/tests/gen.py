"""A field with walls: a seed and a mode. Mode 1 gives a small field with
a few walls, mode 2 a 10 by 10 field with many walls, mode 3 a field
with no walls at all, mode 4 a field cut by a long wall with one gap.
A wall section with no walls is sometimes left out."""

import random
import sys

SIZE = 10


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        width, height = rng.randint(2, 4), rng.randint(2, 4)
    else:
        width, height = SIZE, SIZE
    vertical, horizontal = set(), set()
    if mode in (1, 2):
        share = rng.random() * (0.6 if mode == 2 else 0.3)
        for n in range(1, width):
            for m in range(1, height + 1):
                if rng.random() < share:
                    vertical.add((n, m))
        for n in range(1, width + 1):
            for m in range(1, height):
                if rng.random() < share:
                    horizontal.add((n, m))
    elif mode == 4:
        column = rng.randint(1, width - 1)
        gap = rng.randint(1, height)
        vertical = {(column, m) for m in range(1, height + 1) if m != gap}
    print(width, height)
    print(rng.randint(1, width), rng.randint(1, height))
    print(rng.randint(1, width), rng.randint(1, height))
    for letter, walls in (("v", vertical), ("h", horizontal)):
        if walls or rng.random() < 0.5:
            print(letter)
            for n, m in sorted(walls, key=lambda w: rng.random()):
                print(n, m)


main()
