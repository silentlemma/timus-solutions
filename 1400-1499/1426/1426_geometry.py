import math
import sys

PAD = 1.0  # width given to a rectangle squeezed onto one line
POINTS = 4


def frame(points, dx, dy):
    """The bounding box with sides along (dx, dy) if every point is on its border."""
    us = [x * dx + y * dy for x, y in points]  # exact integers in the turned frame
    vs = [y * dx - x * dy for x, y in points]
    lo_u, hi_u, lo_v, hi_v = min(us), max(us), min(vs), max(vs)
    if any(u not in (lo_u, hi_u) and v not in (lo_v, hi_v) for u, v in zip(us, vs)):
        return None
    norm = math.hypot(dx, dy)
    # back to real lengths; a flat box gets some width, still holding every point on a side
    lo_u, hi_u, lo_v, hi_v = lo_u / norm, hi_u / norm, lo_v / norm, hi_v / norm
    if hi_u == lo_u:
        hi_u += PAD
    if hi_v == lo_v:
        hi_v += PAD
    ex, ey = dx / norm, dy / norm
    corners = [(lo_u, lo_v), (hi_u, lo_v), (hi_u, hi_v), (lo_u, hi_v)]
    return [(u * ex - v * ey, u * ey + v * ex) for u, v in corners]


def solve(points):
    # the valid turns form a closed set whose ends make two points tie,
    # so the directions between points are enough to try
    dirs = [
        (b[0] - a[0], b[1] - a[1]) for i, a in enumerate(points) for b in points[i + 1 :] if a != b
    ]
    for dx, dy in dirs or [(1, 0)]:
        box = frame(points, dx, dy)
        if box:
            return "+ " + " ".join("%.9f %.9f" % p for p in box)
    return "-"


def main():
    data = sys.stdin.read().split()
    n = int(data[0])
    vals = iter(map(int, data[1:]))
    out = []
    for _ in range(n):
        pts = [(next(vals), next(vals)) for _ in range(POINTS)]
        out.append(solve(pts))
    sys.stdout.write("".join(line + "\n" for line in out))


main()
