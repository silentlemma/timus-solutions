"""A random convex polygon: a seed, N and the half-axes of an ellipse
(RX RY); the vertices are N random points of the rotated ellipse in
counterclockwise order, rounded to three decimals."""

import math
import random
import sys


def main():
    seed, n = int(sys.argv[1]), int(sys.argv[2])
    rx, ry = float(sys.argv[3]), float(sys.argv[4])
    rng = random.Random(seed)
    while True:
        rot = rng.uniform(0, math.pi)
        cx, cy = rng.uniform(-5, 5), rng.uniform(-5, 5)
        angles = sorted(rng.uniform(0, 2 * math.pi) for _ in range(n))
        pts = []
        for a in angles:
            x, y = rx * math.cos(a), ry * math.sin(a)
            px = cx + x * math.cos(rot) - y * math.sin(rot)
            py = cy + x * math.sin(rot) + y * math.cos(rot)
            pts.append((round(px, 3), round(py, 3)))
        if len(set(pts)) == n and all(abs(v) <= 100 for p in pts for v in p):
            break
    lines = [str(n)] + ["%.3f %.3f" % p for p in pts]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
