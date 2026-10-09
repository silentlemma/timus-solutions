"""A random country: a seed, L, A, the number of plots, their largest side
and the share of jury plots in percent. Plots never overlap."""

import random
import sys

JURY = 255
PERCENT = 100
TOP = 100
LOWEST = 2
TRIES = 100000


def main():
    seed, size, park, count, largest, jury = (int(x) for x in sys.argv[1:7])
    rng = random.Random(seed)
    plots = []
    for _ in range(TRIES):
        if len(plots) == count:
            break
        s = rng.randint(1, min(largest, size))
        x, y = rng.randint(1, size - s + 1), rng.randint(1, size - s + 1)
        if any(
            x < px + ps and px < x + s and y < py + ps and py < y + s for _, ps, px, py in plots
        ):
            continue
        w = JURY if rng.randrange(PERCENT) < jury else rng.randint(LOWEST, TOP)
        plots.append((w, s, x, y))
    lines = ["%d %d" % (size, park), str(len(plots))] + ["%d %d %d %d" % p for p in plots]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
