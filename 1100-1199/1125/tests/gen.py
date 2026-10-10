"""Random games: a seed, M, N, the largest visit count and the share of
cells visited at all, in per cent."""

import random
import sys

PERCENT = 100


def main():
    seed, m, n, top, share = (int(x) for x in sys.argv[1:6])
    rng = random.Random(seed)
    lines = ["%d %d" % (m, n)]
    lines += ["".join(rng.choice("WB") for _ in range(n)) for _ in range(m)]
    for _ in range(m):
        row = [rng.randint(0, top) if rng.randrange(PERCENT) < share else 0 for _ in range(n)]
        lines.append(" ".join(map(str, row)))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
