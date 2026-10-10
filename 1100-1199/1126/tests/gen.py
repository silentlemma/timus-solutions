"""Random readings: a seed, M, N and a mode. Mode 0 draws any values,
mode 1 rises steadily, mode 2 falls steadily, mode 3 has calm stretches
broken by short storms of high peaks."""

import random
import sys

TOP = 100000
CALM = 20
STORM = 0.02


def main():
    seed, m, n, mode = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    if mode == 1:
        values = sorted(rng.randint(0, TOP) for _ in range(n))
    elif mode == 2:
        values = sorted((rng.randint(0, TOP) for _ in range(n)), reverse=True)
    elif mode == 3:
        values = [
            rng.randint(TOP // 2, TOP) if rng.random() < STORM else rng.randint(0, CALM)
            for _ in range(n)
        ]
    else:
        values = [rng.randint(0, TOP) for _ in range(n)]
    sys.stdout.write("\n".join(map(str, [m] + values + [-1])) + "\n")


if __name__ == "__main__":
    main()
