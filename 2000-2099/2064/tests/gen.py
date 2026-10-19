"""Caterpillars and queries from a seed and a mode: 1 a few small ones,
2 many small values, 3 values around the queries, 4 the largest input with
values up to 10^9, 5 the largest input with values below the queries, 6 a
single caterpillar taller than every query."""

import random
import sys

MOST = 10 ** 6
TALL = 10 ** 9


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n, q, top, xs = rng.randint(1, 5), rng.randint(1, 30), 20, 40
    elif mode == 2:
        n, q, top, xs = 1000, 1000, 100, 1000
    elif mode == 3:
        n, q, top, xs = 2000, 2000, 5000, 5000
    elif mode == 4:
        n, q, top, xs = MOST, MOST, TALL, MOST
    elif mode == 5:
        n, q, top, xs = MOST, MOST, MOST // 3, MOST
    else:
        n, q, top, xs = 1, 1000, TALL, MOST
    if mode == 6:
        t = [TALL]
    else:
        t = [rng.randint(1, top) for _ in range(n)]
    x = [rng.randint(1, xs) for _ in range(q)]
    out = [str(n), " ".join(map(str, t)), str(q)] + [str(v) for v in x]
    sys.stdout.write("\n".join(out) + "\n")


main()
