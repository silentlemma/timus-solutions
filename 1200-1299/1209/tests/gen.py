"""Positions: a seed, N and a mode. Mode 1 draws them anywhere, mode 2
around the ones, mode 3 lists 1, 2, ..., N."""

import random
import sys

TOP = 2**31 - 1


def main():
    seed, n, mode = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    if mode == 1:
        ks = [rng.randint(1, TOP) for _ in range(n)]
    elif mode == 2:
        ks = []
        while len(ks) < n:
            m = rng.randint(1, 65536)
            k = 1 + m * (m - 1) // 2 + rng.randint(-1, 1)
            if 1 <= k <= TOP:
                ks.append(k)
    else:
        ks = list(range(1, n + 1))
    sys.stdout.write("\n".join(map(str, [n] + ks)) + "\n")


if __name__ == "__main__":
    main()
