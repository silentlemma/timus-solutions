"""Cubes and a figure: a seed and a mode. Mode 1 builds every cell from a
different cube, turned at random, with some faces left free (always
solvable); mode 2 draws the demands at random from few colours (often
not solvable); mode 3 uses two colours on 30 cubes and 30 cells, so that
many cubes fit many cells and the matching has to shuffle."""

import random
import sys

FACES = 6
TOP = 30
SPIN = (2, 1, 5, 3, 0, 4)
TIP = (1, 5, 2, 0, 4, 3)


def turn(cube, rng):
    for _ in range(rng.randint(0, 8)):
        g = rng.choice([SPIN, TIP])
        cube = [cube[g[f]] for f in range(FACES)]
    return cube


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    colours = {1: TOP, 2: 3, 3: 2}[mode]
    n = rng.randint(1, TOP) if mode != 3 else TOP
    cubes = [[rng.randint(1, colours) for _ in range(FACES)] for _ in range(n)]
    m = rng.randint(1, n) if mode != 3 else TOP
    cells = []
    if mode == 1:
        for c in rng.sample(range(n), m):
            need = turn(cubes[c], rng)
            cells.append([x if rng.random() < 0.6 else 0 for x in need])
    else:
        for _ in range(m):
            cells.append([rng.randint(0, colours) for _ in range(FACES)])
    places = rng.sample([(x, y, z) for x in range(4) for y in range(4) for z in range(4)], m)
    out = ["%d" % n] + [" ".join(map(str, c)) for c in cubes] + ["%d" % m]
    out += ["%d %d %d %s" % (*p, " ".join(map(str, c))) for p, c in zip(places, cells)]
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
