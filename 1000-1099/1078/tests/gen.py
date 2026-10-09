"""Random segments: a seed, N, the largest coordinate and the shape (0 any
segments, 1 a long nested chain hidden among random ones)."""

import random
import sys

ANY, CHAIN = 0, 1


def main():
    seed, n, top, shape = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    segs = []
    if shape == CHAIN:
        # half of the segments nest around a common centre, with random gaps
        lo = hi = rng.randint(-top // 2, top // 2)
        for _ in range(n // 2):
            segs.append((lo, hi))
            lo -= rng.randint(1, 2)
            hi += rng.randint(1, 2)
            if lo < -top or hi > top:
                break
    while len(segs) < n:
        a, b = rng.randint(-top, top), rng.randint(-top, top)
        segs.append((min(a, b), max(a, b)))
    rng.shuffle(segs)
    sys.stdout.write("\n".join([str(n)] + ["%d %d" % s for s in segs]) + "\n")


if __name__ == "__main__":
    main()
