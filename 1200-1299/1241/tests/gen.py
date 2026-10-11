"""A plate and its cuts: a seed, M, N and a share of all possible cuts in
percent (100 takes every one). Each cut is written from one border point
to the other, in either order."""

import random
import sys

PERCENT = 100


def ends(m, n, kind, c):
    """The two border points of a cut line."""
    if kind == "x":
        return (c, 0), (c, n)
    if kind == "y":
        return (0, c), (m, c)
    on = []
    for x in range(m + 1):
        y = x - c if kind == "d" else c - x
        if 0 <= y <= n and (x in (0, m) or y in (0, n)):
            on.append((x, y))
    on.sort()
    return on[0], on[-1]


def main():
    seed, m, n, share = (int(v) for v in sys.argv[1:5])
    rng = random.Random(seed)
    lines = [("x", c) for c in range(1, m)] + [("y", c) for c in range(1, n)]
    lines += [("d", c) for c in range(-n + 1, m)] + [("s", c) for c in range(1, m + n)]
    chosen = [line for line in lines if rng.randrange(PERCENT) < share]
    rng.shuffle(chosen)
    out = ["%d %d %d" % (m, n, len(chosen))]
    for kind, c in chosen:
        a, b = ends(m, n, kind, c)
        if rng.random() < 0.5:
            a, b = b, a
        out.append("%d %d %d %d" % (*a, *b))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
