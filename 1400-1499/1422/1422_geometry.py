import sys
from math import gcd


def main():
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    vals = iter(map(int, data[1:]))
    points = list(zip(vals, vals, vals))
    best = 1
    for i, (x, y, z) in enumerate(points):
        if n - i <= best:
            break  # no line through a later first point can beat best
        same = 0
        lines = {}
        for px, py, pz in points[i + 1 :]:
            dx, dy, dz = px - x, py - y, pz - z
            g = gcd(dx, dy, dz)
            if g == 0:
                same += 1  # several flies may hang at one point
                continue
            # one key per direction: reduced, with the first non-zero part positive
            if dx < 0 or dx == 0 and (dy < 0 or dy == 0 and dz < 0):
                g = -g
            key = (dx // g, dy // g, dz // g)
            lines[key] = lines.get(key, 0) + 1
        best = max(best, 1 + same + max(lines.values(), default=0))
    print(best)


main()
