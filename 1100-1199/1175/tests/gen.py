"""Sequence parameters that keep every H within 0..100000: a seed, a bound M
on the terms and a mode. Mode 0 picks random A1..A4 small enough for M,
mode 1 adds the last two terms modulo M + 1 (a Fibonacci-like sequence),
mode 2 uses only the last term, a*X + b modulo M + 1, mode 3 lets H stay
below B1 for a while before folding."""

import random
import sys

LIMIT = 100000


def main():
    seed, m, mode = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    c = m + 1
    b1 = b2 = m
    a1 = a2 = a3 = a4 = 0
    if mode == 1:
        a2 = a3 = 1
    elif mode == 2:
        a3 = rng.randint(1, max(1, LIMIT // c - 1))
        a4 = rng.randint(0, m)
    else:
        if mode == 3:
            b1 = rng.randint(m, 2 * m)
            c = rng.randint(1, m + 1)
        top = max(b1, 1)
        a1 = rng.randint(0, LIMIT // (4 * top * top))
        rest = LIMIT - a1 * top * top
        a2 = rng.randint(0, rest // (3 * top))
        a3 = rng.randint(0, rest // (3 * top))
        a4 = rng.randint(0, rest // 3)
    # terms never exceed max(B1, B2), so every H stays within the limit
    top = max(b1, b2)
    assert a1 * top * top + a2 * top + a3 * top + a4 <= LIMIT, "parameters too large"
    x1, x2 = rng.randint(0, m), rng.randint(0, m)
    sys.stdout.write("%d %d %d %d %d %d %d\n%d %d\n" % (a1, a2, a3, a4, b1, b2, c, x1, x2))


if __name__ == "__main__":
    main()
