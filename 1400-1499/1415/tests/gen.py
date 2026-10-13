"""Stations and routes: a seed and a mode. Mode 1 spreads 100 stations
of radius up to 1000 over the whole town and drives 1000 random
segments, mode 2 packs 100 small stations into a 300 by 300 square,
mode 3 puts stations on one line so that several reach the red circle
at the same moment, mode 4 mixes zero-length segments and
back-and-forth driving near a few stations, mode 5 uses 100 wide cells
with radii up to the maximum 10000 and 1000 segments across the town,
mode 6 crosses a chain of 100 overlapping cells in both directions.
A route point or segment
that comes within 0.0001 of a level circle is drawn again."""

import math
import random
import string
import sys

LIMIT = 10000
STATIONS = 100
SEGMENTS = 1000
GAP = 1e-4
STEPS = 5
LEVELS = 6


def circles(r):
    return [r * 10 ** (k / STEPS) for k in range(LEVELS)]


def near(stations, d_of):
    return any(abs(d_of(x, y) - c) < GAP for x, y, r, _ in stations for c in circles(r))


def point_ok(stations, p):
    return not near(stations, lambda x, y: math.hypot(p[0] - x, p[1] - y))


def segment_ok(stations, a, b):
    """No end on a circle and no circle touching the segment."""
    if not point_ok(stations, b):
        return False
    dx, dy = b[0] - a[0], b[1] - a[1]
    if dx == dy == 0:
        return True
    for x, y, r, _ in stations:
        t = ((x - a[0]) * dx + (y - a[1]) * dy) / (dx * dx + dy * dy)
        if 0 < t < 1:
            d = math.hypot(a[0] + dx * t - x, a[1] + dy * t - y)
            if any(abs(d - c) < GAP for c in circles(r)):
                return False
    return True


def names(rng, count):
    seen = set()
    while len(seen) < count:
        seen.add(
            "".join(
                rng.choice(string.ascii_letters + "_0123456789") for _ in range(rng.randint(1, 8))
            )
        )
    return sorted(seen, key=lambda _: rng.random())


def route_of(rng, stations, pick, stay=0.0):
    route = [pick()]
    while not point_ok(stations, route[0]):
        route = [pick()]
    while len(route) < SEGMENTS + 1:
        p = route[-1] if rng.random() < stay else pick()
        if segment_ok(stations, route[-1], p):
            route.append(p)
    return route


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        stations = [
            (rng.randint(-LIMIT, LIMIT), rng.randint(-LIMIT, LIMIT), rng.randint(1, 1000), nm)
            for nm in names(rng, STATIONS)
        ]
        route = route_of(
            rng, stations, lambda: (rng.randint(-LIMIT, LIMIT), rng.randint(-LIMIT, LIMIT))
        )
    elif mode == 2:
        stations = [
            (rng.randint(0, 300), rng.randint(0, 300), rng.randint(1, 10), nm)
            for nm in names(rng, STATIONS)
        ]
        route = route_of(rng, stations, lambda: (rng.randint(-50, 350), rng.randint(-50, 350)))
    elif mode == 3:
        # x + 10 r is the same for every station: all turn non-red together
        reach = 1000
        stations = []
        for nm in names(rng, 30):
            r = rng.randint(2, 60)
            stations.append((reach - 10 * r, 0, r, nm))
        route = [(3000, 0), (-3000, 0), (3000, 0)]
    elif mode == 5:
        stations = [(-LIMIT, -LIMIT, LIMIT, "Wide_000")]
        stations += [
            (rng.randint(-LIMIT, LIMIT), rng.randint(-LIMIT, LIMIT),
             rng.randint(8000, LIMIT), f"Wide_{i:03d}")
            for i in range(1, STATIONS)
        ]
        route = route_of(
            rng, stations, lambda: (rng.randint(-LIMIT, LIMIT), rng.randint(-LIMIT, LIMIT))
        )
    elif mode == 6:
        stations = [
            (-9000 + 180 * i, 0, rng.randint(11, 17), f"Chain_{i:03d}")
            for i in range(STATIONS)
        ]
        route = [(-9500, 1), (9500, 1), (-9500, 2), (9500, 3)]
    else:
        stations = [
            (rng.randint(-50, 50), rng.randint(-50, 50), rng.randint(1, 5), nm)
            for nm in names(rng, 5)
        ]
        route = route_of(rng, stations, lambda: (rng.randint(-80, 80), rng.randint(-80, 80)), 0.2)
    print(len(stations))
    for x, y, r, nm in stations:
        print(x, y, r, nm)
    print(len(route) - 1)
    for (ax, ay), (bx, by) in zip(route, route[1:]):
        print(ax, ay, bx, by)


main()
