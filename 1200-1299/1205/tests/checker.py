"""Checker: the printed time must match the time of the printed route,
walking from A to the first station, riding between linked stations,
walking between unlinked ones and walking from the last station to B;
and it must equal the reference's time. Both within 1e-6."""

import sys
from math import hypot

TOL = 1e-6


def fail(reason):
    print(reason)
    sys.exit(1)


def read_input(path):
    data = open(path).read().split()
    walk, metro, n = float(data[0]), float(data[1]), int(data[2])
    pts = [(float(data[3 + 2 * i]), float(data[4 + 2 * i])) for i in range(n)]
    pos = 3 + 2 * n
    linked = set()
    while True:
        a, b = int(data[pos]), int(data[pos + 1])
        pos += 2
        if a == 0 and b == 0:
            break
        linked |= {(a, b), (b, a)}
    a = (float(data[pos]), float(data[pos + 1]))
    b = (float(data[pos + 2]), float(data[pos + 3]))
    return walk, metro, pts, linked, a, b


def read_answer(path, n):
    try:
        tokens = open(path).read().split()
        time = float(tokens[0])
        count = int(tokens[1])
        route = [int(t) for t in tokens[2:]]
    except (ValueError, IndexError):
        fail("expected a time, a count and station numbers")
    if count != len(route) or any(not 1 <= s <= n for s in route):
        fail("the route does not match its count or names a missing station")
    return time, route


def main():
    inp, ans, output = sys.argv[1:4]
    walk, metro, pts, linked, a, b = read_input(inp)
    best, _ = read_answer(ans, len(pts))
    time, route = read_answer(output, len(pts))
    places = [a] + [pts[s - 1] for s in route] + [b]
    stops = [0] + route + [0]
    total = 0.0
    for i in range(len(places) - 1):
        (x1, y1), (x2, y2) = places[i], places[i + 1]
        speed = metro if (stops[i], stops[i + 1]) in linked else walk
        total += hypot(x2 - x1, y2 - y1) / speed
    slack = TOL * max(1.0, best)
    if abs(total - time) > slack:
        fail("the route takes %.9f, but %.9f is printed" % (total, time))
    if abs(time - best) > slack:
        fail("time %.9f, expected %.9f" % (time, best))


if __name__ == "__main__":
    main()
