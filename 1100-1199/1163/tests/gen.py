"""Eight red and eight white draughts that neither overlap nor touch and
stay inside the board: a seed and a mode. Mode 0 places them at random,
mode 1 on random cell centres, mode 2 in two clusters, one per colour,
mode 3 along the edges of the board."""

import random
import sys

SIDE = 8
RADIUS = 0.4
GAP = 0.81
TOP = SIDE - RADIUS


def spot(rng, mode, colour):
    if mode == 1:
        return rng.randrange(SIDE) + 0.5, rng.randrange(SIDE) + 0.5
    if mode == 2:
        cx = 2 if colour == 0 else 6
        return round(rng.uniform(cx - 1.6, cx + 1.6), 2), round(rng.uniform(RADIUS, TOP), 2)
    if mode == 3:
        t = round(rng.uniform(RADIUS, TOP), 2)
        side = rng.randrange(4)
        return [(t, RADIUS), (t, TOP), (RADIUS, t), (TOP, t)][side]
    return round(rng.uniform(RADIUS, TOP), 2), round(rng.uniform(RADIUS, TOP), 2)


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    pts = []
    while len(pts) < 2 * SIDE:
        x, y = spot(rng, mode, len(pts) // SIDE)
        if all((x - a) ** 2 + (y - b) ** 2 > GAP for a, b in pts):
            pts.append((x, y))
    lines = [" ".join("%g %g" % p for p in pts[k : k + SIDE]) for k in (0, SIDE)]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
