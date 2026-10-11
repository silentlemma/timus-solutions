"""Queries: a seed, their number and a mode. Mode 1 draws eggs and floors
up to 1000, mode 2 lists every pair up to a small bound, mode 3 uses few
eggs and many floors, mode 4 draws 4..9 eggs and 32..1000 floors, and
mode 5 interleaves repeated queries with scarce and plentiful eggs at
the same random floor count. In mode 2, count is the bound; otherwise
it is the number of queries."""

import random
import sys

TOP = 1000


def main():
    seed, count, mode = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    if mode == 2:
        pairs = [(e, f) for e in range(1, count + 1) for f in range(1, count + 1)]
    elif mode == 3:
        pairs = [(rng.randint(1, 3), rng.randint(1, TOP)) for _ in range(count)]
    elif mode == 4:
        pairs = [(rng.randint(4, 9), rng.randint(32, TOP)) for _ in range(count)]
    elif mode == 5:
        pairs = []
        while len(pairs) < count:
            floors = rng.randint(32, TOP)
            scarce = rng.randint(1, 8)
            plentiful = rng.choice((10, 11, TOP - 1, TOP))
            pairs.extend(((scarce, floors), (plentiful, floors), (scarce, floors)))
        pairs = pairs[:count]
    else:
        pairs = [(rng.randint(1, TOP), rng.randint(1, TOP)) for _ in range(count)]
    lines = ["%d %d" % p for p in pairs] + ["0 0"]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
