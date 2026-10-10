"""Boxes for the generals: a seed, N, M, K and a mode. Mode 0 takes values
from 1 to 1000, mode 1 from 1 to 10, mode 2 makes all values equal, mode
3 takes values from 900 to 1000."""

import random
import sys

TOP = 1000
SMALL = 10
HIGH = 900


def main():
    seed, n, m, k, mode = (int(x) for x in sys.argv[1:6])
    rng = random.Random(seed)
    if mode == 1:
        values = [rng.randint(1, SMALL) for _ in range(n)]
    elif mode == 2:
        values = [rng.randint(1, TOP)] * n
    elif mode == 3:
        values = [rng.randint(HIGH, TOP) for _ in range(n)]
    else:
        values = [rng.randint(1, TOP) for _ in range(n)]
    sys.stdout.write("%d %d %d\n%s\n" % (n, m, k, " ".join(map(str, values))))


if __name__ == "__main__":
    main()
