"""N cities with no three on a line: a seed, N and a mode. The cities are
points (t, t^2) of a parabola for distinct t, which never has three
points on a line, moved by an integer linear map with nonzero determinant
so they stay on a conic. Mode 0 keeps the parabola, mode 1 applies a
random map, mode 2 swaps the axes, which gives many pairs of cities the
same x."""

import random
import sys

LIMIT = 10**9
COEF = 3


def main():
    seed, n, mode = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
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
