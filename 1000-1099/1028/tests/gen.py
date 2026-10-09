"""Distinct stars listed by Y, then X.

Modes:
  SEED N TOP: uniform random stars, coordinates from 0 through TOP (legacy).
  alternating N: alternate x=32000 and x=0 at increasing y, 1 <= N <= 15000.
  bands SEED N: random stars in eight boundary columns, 4 <= N <= 15000.
"""

import random
import sys


def main():
    if sys.argv[1] == "alternating":
        n = int(sys.argv[2])
        assert 1 <= n <= 15000
        stars = [(32000 if i % 2 == 0 else 0, i * 32000 // max(1, n - 1))
                 for i in range(n)]
        print("\n".join([str(n)] + ["%d %d" % s for s in stars]))
        return
    if sys.argv[1] == "bands":
        seed, n = map(int, sys.argv[2:4])
        assert 4 <= n <= 15000
        rng = random.Random(seed)
        columns = (0, 1, 2, 16383, 16384, 16385, 31999, 32000)
        stars = {(0, 0), (32000, 0), (0, 32000), (32000, 32000)}
        while len(stars) < n:
            stars.add((rng.choice(columns), rng.randint(0, 32000)))
        lines = [str(n)] + ["%d %d" % s for s in sorted(stars, key=lambda s: (s[1], s[0]))]
        print("\n".join(lines))
        return
    seed, n, top = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    stars = set()
    while len(stars) < n:
        stars.add((rng.randint(0, top), rng.randint(0, top)))
    lines = [str(n)] + ["%d %d" % s for s in sorted(stars, key=lambda s: (s[1], s[0]))]
    print("\n".join(lines))


if __name__ == "__main__":
    main()
