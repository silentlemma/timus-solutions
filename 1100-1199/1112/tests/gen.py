"""Random segments: a seed, N, the coordinate bound and a mode. Mode 0
draws random segments, mode 1 short segments that often touch, mode 2 a
few distinct segments repeated many times, mode 3 nested segments around
a common centre."""

import random
import sys

SHORT = 5


def main():
    seed, n, top, mode = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    segs = []
    pool = []
    for _ in range(n):
        if mode == 1:
            a = rng.randint(-top, top - 1)
            b = min(top, a + rng.randint(1, SHORT))
        elif mode == 2:
            if not pool or rng.random() < 1 / SHORT:
                a = rng.randint(-top, top - 1)
                pool.append((a, rng.randint(a + 1, top)))
            a, b = rng.choice(pool)
        elif mode == 3:
            half = rng.randint(1, top)
            a, b = -half, half
        else:
            a = rng.randint(-top, top - 1)
            b = rng.randint(a + 1, top)
        segs.append((a, b))
    lines = [str(n)] + ["%d %d" % s for s in segs]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
