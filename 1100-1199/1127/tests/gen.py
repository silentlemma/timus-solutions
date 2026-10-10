"""Random cube sets: a seed, N and a mode. Mode 0 paints every cube with
six random colours, mode 1 turns a few base cubes at random so that tall
towers exist, mode 2 mixes rotated copies of one cube with rotated copies
of its mirror image; turned upside down, a mirror image shows the same
ring of sides, so all of them fit in one tower."""

import random
import sys

COLOURS = "ABCGORSVWY"
FACES = 6
BASES = 3
# front, right, left, back, top, bottom; turns as "new position <- old"
SPIN = [2, 0, 3, 1, 4, 5]
TIP = [4, 1, 2, 5, 3, 0]


def turn(cube, rng):
    for _ in range(rng.randint(0, FACES)):
        moves = rng.choice((SPIN, TIP))
        cube = "".join(cube[moves[p]] for p in range(FACES))
    return cube


def main():
    seed, n, mode = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    if mode == 0:
        cubes = ["".join(rng.sample(COLOURS, FACES)) for _ in range(n)]
    else:
        bases = ["".join(rng.sample(COLOURS, FACES)) for _ in range(BASES)]
        if mode == 2:
            # swapping right and left mirrors a cube
            b = bases[0]
            bases = [b, b[0] + b[2] + b[1] + b[3:]]
        cubes = [turn(rng.choice(bases), rng) for _ in range(n)]
    sys.stdout.write("\n".join([str(n)] + cubes) + "\n")


if __name__ == "__main__":
    main()
