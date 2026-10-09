"""A random throw: a seed and the shape (0 anything, 1 aimed at a point
well inside the target, 2 aimed at a point near its edge, 3 a horizontal
target on the ground). Numbers have at most four decimals."""

import math
import random
import sys

ANY, INSIDE, EDGE, GROUND = 0, 1, 2, 3
TOP = 500
HALF_G = 5
DIGITS = 4


def num(x):
    return round(x, DIGITS)


def fmt(xs):
    return " ".join(("%.4f" % x).rstrip("0").rstrip(".") for x in xs)


def main():
    seed, shape = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    while True:
        c = [num(rng.uniform(-TOP / 2, TOP / 2)) for _ in range(3)]
        n = [num(rng.uniform(-1, 1) * rng.choice([1, 10, 100])) for _ in range(3)]
        if shape == GROUND:
            n = [0, 0, num(rng.uniform(0.1, 10))]
        r = num(rng.uniform(0.5, 60))
        s = [num(rng.uniform(-TOP / 2, TOP / 2)) for _ in range(3)]
        if shape == ANY:
            v = [num(rng.uniform(-TOP / 5, TOP / 5)) for _ in range(3)]
        else:
            # a point in the plane at a chosen distance from the centre
            u = [rng.gauss(0, 1) for _ in range(3)]
            nn = sum(x * x for x in n)
            if nn == 0:
                continue
            k = sum(a * b for a, b in zip(u, n)) / nn
            u = [a - k * b for a, b in zip(u, n)]
            norm = math.sqrt(sum(x * x for x in u)) or 1
            rho = r * (rng.uniform(0, 0.9) if shape != EDGE else rng.uniform(0.9999, 1.0001))
            p = [ci + rho * ui / norm for ci, ui in zip(c, u)]
            t = rng.uniform(0.5, 8)
            v = [
                num((p[0] - s[0]) / t),
                num((p[1] - s[1]) / t),
                num((p[2] - s[2] + HALF_G * t * t) / t),
            ]
        if v[0] == 0 and v[1] == 0 or not any(n):
            continue
        if all(abs(x) <= TOP for x in c + n + s + v + [r]):
            break
    sys.stdout.write(fmt(c + n + [r]) + "\n" + fmt(s + v) + "\n")


if __name__ == "__main__":
    main()
