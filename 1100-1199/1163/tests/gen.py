"""Eight red and eight white draughts that neither overlap nor touch and
stay inside the board: a seed and a mode. Mode 0 places them at random,
mode 1 on random cell centres, mode 2 in two clusters, one per colour,
mode 3 along the edges of the board, mode 4 on a nearly touching shuffled
4-by-4 grid, mode 5 on three staggered rails with simultaneous tangencies,
mode 6 around a perturbed circular ring with shuffled colours."""

import math
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
    if mode == 4:
        pts = [
            (round(2.8 + 0.8001 * x + rng.uniform(-0.00001, 0.00001), 6),
             round(2.8 + 0.8001 * y + rng.uniform(-0.00001, 0.00001), 6))
            for x in range(4) for y in range(4)
        ]
    elif mode == 5:
        pts = [(0.5 + 1.4 * k, 3.2) for k in range(6)]
        pts += [(1.2 + 1.4 * k, 4.0) for k in range(5)]
        pts += [(0.5 + 1.4 * k, 4.8) for k in range(5)]
    elif mode == 6:
        phase = rng.uniform(0, 2 * math.pi)
        for k in range(2 * SIDE):
            angle = phase + k * math.pi / SIDE + rng.uniform(-0.02, 0.02)
            radius = rng.uniform(3.48, 3.52)
            pts.append((round(4 + radius * math.cos(angle), 6),
                        round(4 + radius * math.sin(angle), 6)))
    if mode in (4, 5, 6):
        rng.shuffle(pts)
    while len(pts) < 2 * SIDE:
        x, y = spot(rng, mode, len(pts) // SIDE)
        if all((x - a) ** 2 + (y - b) ** 2 > GAP for a, b in pts):
            pts.append((x, y))
    lines = [" ".join("%g %g" % p for p in pts[k : k + SIDE]) for k in (0, SIDE)]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
