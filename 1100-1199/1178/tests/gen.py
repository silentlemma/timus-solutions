"""N cities with no three on a line: a seed, N and a mode.

Modes 0-2 use points (t, t^2) for distinct t, moved by an invertible
integer linear map, so no three become collinear. Mode 0 keeps the
parabola, mode 1 applies a random map, and mode 2 swaps the axes,
giving many pairs the same x. Mode 3 rejection-samples arbitrary points
throughout the coordinate range, checking every previous pair; use it
for small and medium random clouds rather than maximum-size inputs.
"""

import random
import sys

LIMIT = 10**9
COEF = 3


def main():
    seed, n, mode = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    if mode == 3:
        points = []
        while len(points) < n:
            x, y = rng.randint(-LIMIT, LIMIT), rng.randint(-LIMIT, LIMIT)
            if (x, y) in points:
                continue
            if any(
                (bx - ax) * (y - ay) == (by - ay) * (x - ax)
                for i, (ax, ay) in enumerate(points)
                for bx, by in points[i + 1 :]
            ):
                continue
            points.append((x, y))
        sys.stdout.write(str(n) + "\n" + "".join("%d %d\n" % p for p in points))
        return
    if mode == 0:
        a, b, c, d = 1, 0, 0, 1
    elif mode == 2:
        a, b, c, d = 0, 1, 1, 0
    else:
        while True:
            a, b, c, d = (rng.randint(-COEF, COEF) for _ in range(4))
            if a * d - b * c:
                break
    # |a t + b t^2| stays within the limit for |t| up to reach
    reach = int((LIMIT / (2 * COEF)) ** 0.5)
    ts = rng.sample(range(-reach, reach + 1), n)
    lines = [str(n)] + ["%d %d" % (a * t + b * t * t, c * t + d * t * t) for t in ts]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
