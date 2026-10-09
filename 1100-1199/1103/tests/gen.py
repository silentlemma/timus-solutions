"""Random pencils: a seed, an odd N and the largest coordinate. With large
coordinates three points on a line or four on a circle are left to chance,
which is negligible."""

import random
import sys


def main():
    seed, n, top = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    pts = set()
    while len(pts) < n:
        pts.add((rng.randint(-top, top), rng.randint(-top, top)))
    pts = list(pts)
    rng.shuffle(pts)
    sys.stdout.write("\n".join([str(n)] + ["%d %d" % p for p in pts]) + "\n")


if __name__ == "__main__":
    main()
