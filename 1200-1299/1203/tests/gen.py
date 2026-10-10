"""Talks: a seed, N, the largest end time and the longest talk."""

import random
import sys


def main():
    seed, n, top, longest = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    lines = [str(n)]
    for _ in range(n):
        s = rng.randint(1, top - 1)
        lines.append("%d %d" % (s, min(top, s + rng.randint(1, longest))))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
