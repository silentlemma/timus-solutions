"""One test from a seed and a mode: mode 1 a small field, mode 2 a large
square field, mode 3 one fully open row, mode 4 a long winding snake (deep
tree), mode 5 a large field with many short branches. The open cells
grow one at a time next to exactly one open cell, so they form a tree."""

import random
import sys

MOST_CELLS = 100000
MOST_Q = 50000


def grow(rng, h, w, target, bias):
    """Open cells that induce a tree, grown from a random cell; bias > 0
    prefers to extend the newest cell, giving long corridors."""
    def neighbours(v):
        r, c = divmod(v, w)
        if r > 0:
            yield v - w
        if r < h - 1:
            yield v + w
        if c > 0:
            yield v - 1
        if c < w - 1:
            yield v + 1

    open_cell = [False] * (h * w)
    start = rng.randrange(h * w)
    open_cell[start] = True
    cells = [start]
    tries = 0
    while len(cells) < target and tries < 20 * target:
        tries += 1
        base = cells[-1] if rng.random() < bias else rng.choice(cells)
        options = [u for u in neighbours(base) if not open_cell[u]
                   and sum(open_cell[x] for x in neighbours(u)) == 1]
        if options:
            u = rng.choice(options)
            open_cell[u] = True
            cells.append(u)
    return open_cell, cells


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        h, w, q = rng.randint(1, 7), rng.randint(1, 7), rng.randint(1, 30)
        bias = 0.3
    elif mode == 3:
        h, w, q, bias = 1, MOST_CELLS, MOST_Q, 0.0
    else:
        h = w = 316
        q, bias = MOST_Q, {2: 0.3, 4: 0.97, 5: 0.0}[mode]
    if mode == 3:
        open_cell, cells = [True] * w, list(range(w))
    else:
        open_cell, cells = grow(rng, h, w, h * w, bias)
    print(h, w)
    for r in range(h):
        print("".join("#" if open_cell[r * w + c] else "." for c in range(w)))
    print(q)
    for _ in range(q):
        a, b = rng.choice(cells), rng.choice(cells)
        print(a // w + 1, a % w + 1, b // w + 1, b % w + 1)


main()
