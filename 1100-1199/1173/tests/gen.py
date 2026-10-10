"""Wally's house and N friends with no three of the N + 1 points on a line:
a seed, N and a mode. Mode 0 scatters everyone in the whole square, mode 1
puts the house in the middle of the friends, mode 2 puts it far to one
side, mode 3 puts the friends near a circle around the house in the middle. Coordinates
have three decimals; points making a line with others are drawn again."""

import random
import sys
from math import cos, gcd, pi, sin

LIMIT = 100000
SCALE = 1000


def direction(p, q):
    dx, dy = q[0] - p[0], q[1] - p[1]
    g = gcd(dx, dy)
    dx, dy = dx // g, dy // g
    # a line, not a ray: both senses give the same key
    return (dx, dy) if dx > 0 or (dx == 0 and dy > 0) else (-dx, -dy)


def fits(points, p):
    if p in points:
        return False
    seen = set()
    for q in points:
        d = direction(p, q)
        if d in seen:
            return False
        seen.add(d)
    return True


def main():
    seed, n, mode = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    span = LIMIT * SCALE

    def anywhere(lo=-span, hi=span):
        return (rng.randint(lo, hi), rng.randint(lo, hi))

    if mode in (1, 3):
        house = (0, 0)
    elif mode == 2:
        house = (-span, rng.randint(-span, span))
    else:
        house = anywhere()
    points = [house]
    while len(points) < n + 1:
        if mode == 2:
            p = anywhere(0, span)
        elif mode == 3:
            angle = rng.uniform(0, 2 * pi)
            radius = span // 2 + rng.randint(0, span // 100)
            p = (int(radius * cos(angle)), int(radius * sin(angle)))
        else:
            p = anywhere()
        if all(abs(v) <= span for v in p) and fits(points, p):
            points.append(p)
    ids = list(range(1, n + 1))
    rng.shuffle(ids)

    def show(v):
        return "%d.%03d" % (v // SCALE, v % SCALE) if v >= 0 else "-" + show(-v)

    lines = ["%s %s" % (show(house[0]), show(house[1])), str(n)]
    lines += ["%s %s %d" % (show(x), show(y), i) for (x, y), i in zip(points[1:], ids)]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
