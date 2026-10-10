"""Deterministic cables, written in metres with exactly two decimals.

Modes:
  SEED N K TOP: draw N lengths uniformly from 100 through TOP centimetres.
  equal N K LENGTH: print N identical cables of LENGTH centimetres.
"""

import random
import sys

CENTS = 100


def main():
    if sys.argv[1] == "equal":
        n, k, length = map(int, sys.argv[2:5])
        cable = "%d.%02d" % divmod(length, CENTS)
        sys.stdout.write("%d %d\n" % (n, k) + (cable + "\n") * n)
        return

    seed, n, k, top = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    lines = ["%d %d" % (n, k)]
    for _ in range(n):
        lines.append("%d.%02d" % divmod(rng.randint(CENTS, top), CENTS))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
