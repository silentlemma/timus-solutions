"""Cables in stock: a seed, N, K and the longest cable in centimetres;
lengths are drawn from 100 cm up to that and written in metres with two
decimals."""

import random
import sys

CENTS = 100


def main():
    seed, n, k, top = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    lines = ["%d %d" % (n, k)]
    for _ in range(n):
        lines.append("%d.%02d" % divmod(rng.randint(CENTS, top), CENTS))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
