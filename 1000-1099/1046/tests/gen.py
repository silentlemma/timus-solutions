"""A random polygon: a seed, N, the radius and the angle mode. The vertices
are random points on a circle in clockwise order; the apexes are computed
from them and rounded to two decimals. Angle modes: small (the total is
below 360, so no subset sums to a multiple of 360), any (angles below 180,
for small N, every subset checked)."""

import cmath
import math
import random
import sys

LIMIT = 100
FULL = 36000  # 360 degrees in hundredths


def subsets_ok(hundredths):
    sums = {0}
    for a in hundredths:
        new = {(s + a) % FULL for s in sums}
        if 0 in new:
            return False
        sums |= new
    return True


def main():
    seed, n, radius = (int(x) for x in sys.argv[1:4])
    mode = sys.argv[4]
    rng = random.Random(seed)
    while True:
        phis = sorted((rng.uniform(0, 2 * math.pi) for _ in range(n)), reverse=True)
        cx, cy = rng.uniform(-10, 10), rng.uniform(-10, 10)
        pts = [complex(cx + radius * math.cos(p), cy + radius * math.sin(p)) for p in phis]
        if mode == "small":
            cap = 36000 // n - 1
            hundredths = [rng.randint(cap // 3, cap) for _ in range(n)]
        else:
            hundredths = [rng.randint(1000, 17900) for _ in range(n)]
            if not subsets_ok(hundredths):
                continue
        apexes = []
        for i in range(n):
            w = cmath.exp(1j * math.radians(hundredths[i] / 100))
            a, b = pts[i], pts[(i + 1) % n]
            apexes.append((b - w * a) / (1 - w))
        if all(abs(m.real) <= LIMIT and abs(m.imag) <= LIMIT for m in apexes):
            break
    lines = [str(n)] + ["%.2f %.2f" % (m.real, m.imag) for m in apexes]
    lines += ["%d.%02d" % divmod(h, 100) for h in hundredths]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
