"""One test from a seed and a mode. Mode 1 is 5000 random joints and 5000
random points, mode 2 a route that winds around the centre several times,
with points near the centre and on the tracks, mode 3 joints on the
border of the square of side 2·10^9, mode 4 a small random route with
points on its joints and tracks, mode 5 a route going there and back."""

import math
import random
import sys

MOST = 5000
FAR = 10**9
SMALL = 6
NEAR = 1000
MOST_LAPS = 6


def on_tracks(rng, pts, count):
    """Points on the tracks: joints and integer points inside segments."""
    out = []
    for _ in range(count):
        i = rng.randrange(len(pts))
        (ax, ay), (bx, by) = pts[i], pts[(i + 1) % len(pts)]
        g = math.gcd(bx - ax, by - ay)
        if g == 0:
            out.append((ax, ay))
            continue
        k = rng.randint(0, g)
        out.append((ax + (bx - ax) // g * k, ay + (by - ay) // g * k))
    return out


def edge_value(rng):
    return rng.choice([-FAR, FAR, rng.randint(-FAR, FAR)])


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        pts = [(rng.randint(-FAR, FAR), rng.randint(-FAR, FAR)) for _ in range(MOST)]
        queries = [(rng.randint(-FAR, FAR), rng.randint(-FAR, FAR)) for _ in range(MOST)]
    elif mode == 2:
        laps = rng.randint(1, MOST_LAPS) * rng.choice([1, -1])
        radius = FAR // 2
        pts = []
        for i in range(MOST):
            angle = 2 * math.pi * laps * i / MOST
            pts.append((round(radius * math.cos(angle)), round(radius * math.sin(angle))))
        queries = [(rng.randint(-NEAR, NEAR), rng.randint(-NEAR, NEAR)) for _ in range(MOST // 2)]
        queries += on_tracks(rng, pts, MOST // 2)
    elif mode == 3:
        pts = [(edge_value(rng), edge_value(rng)) for _ in range(MOST)]
        queries = [(edge_value(rng), edge_value(rng)) for _ in range(MOST)]
    elif mode == 4:
        n = rng.randint(3, 10)
        pts = [(rng.randint(-SMALL, SMALL), rng.randint(-SMALL, SMALL)) for _ in range(n)]
        queries = [(rng.randint(-SMALL, SMALL), rng.randint(-SMALL, SMALL)) for _ in range(20)]
        queries += on_tracks(rng, pts, 10)
    else:
        half = [
            (rng.randint(-NEAR, NEAR), rng.randint(-NEAR, NEAR)) for _ in range(rng.randint(2, 30))
        ]
        pts = half + half[::-1]
        queries = [(rng.randint(-NEAR, NEAR), rng.randint(-NEAR, NEAR)) for _ in range(200)]
    print(len(pts))
    for x, y in pts:
        print(x, y)
    print(len(queries))
    for x, y in queries:
        print(x, y)


main()
