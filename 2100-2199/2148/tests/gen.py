"""Tank and players from "MODE SEED": mode 1 small coordinates, mode 2
coordinates up to the limit, mode 3 small coordinates with players far
apart around the tank; the players are lattice points at the same
distance from the centre."""

import math
import random
import sys

LIMIT = 3000
SMALL = 12
WIDE = 3


def lattice_ring(cx, cy, square, bound):
    radius = math.isqrt(square)
    ring = []
    for dx in range(-radius, radius + 1):
        rest = square - dx * dx
        dy = math.isqrt(rest)
        if dy * dy != rest:
            continue
        for sy in {dy, -dy}:
            x, y = cx + dx, cy + sy
            if abs(x) <= bound and abs(y) <= bound:
                ring.append((x, y))
    return ring


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    bound = LIMIT if mode == 2 else SMALL
    while True:
        cx, cy = rng.randint(-bound, bound), rng.randint(-bound, bound)
        r = rng.randint(1, max(1, bound // (WIDE if mode == 3 else 2)))
        ax, ay = rng.randint(-bound, bound), rng.randint(-bound, bound)
        square = (ax - cx) ** 2 + (ay - cy) ** 2
        if square <= r * r:
            continue
        ring = [p for p in lattice_ring(cx, cy, square, bound) if p != (ax, ay)]
        if not ring:
            continue
        if mode == 3:
            ring.sort(key=lambda p: (p[0] - cx) * (ax - cx) + (p[1] - cy) * (ay - cy))
            bx, by = ring[0]
        else:
            bx, by = rng.choice(ring)
        break
    print(cx, cy, r)
    print(ax, ay)
    print(bx, by)


main()
