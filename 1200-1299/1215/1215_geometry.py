import sys
from math import hypot, sqrt


def segment_distance(px, py, ax, ay, bx, by):
    dx, dy = bx - ax, by - ay
    t = (px - ax) * dx + (py - ay) * dy
    length2 = dx * dx + dy * dy
    if t <= 0:
        return hypot(px - ax, py - ay)
    if t >= length2:
        return hypot(px - bx, py - by)
    return abs((px - ax) * dy - (py - ay) * dx) / sqrt(length2)


def main():
    it = iter(sys.stdin.read().split())
    px, py, n = int(next(it)), int(next(it)), int(next(it))
    pts = [(int(next(it)), int(next(it))) for _ in range(n)]
    edges = [(pts[i], pts[(i + 1) % n]) for i in range(n)]
    # inside a counterclockwise polygon the point is left of every edge
    if all((bx - ax) * (py - ay) - (by - ay) * (px - ax) >= 0 for (ax, ay), (bx, by) in edges):
        print("0.000")
        return
    best = min(segment_distance(px, py, ax, ay, bx, by) for (ax, ay), (bx, by) in edges)
    print("%.3f" % (2 * best))


main()
