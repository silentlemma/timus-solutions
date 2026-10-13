"""Mazes of at most 300 x 30: a seed and a mode. Mode 1 is a perfect maze
with no cycles, mode 2 a perfect maze with rings and blocks carved in,
mode 3 random cells, three in five free, mode 4 random cells, nine in ten
free, mode 5 a serpentine corridor with a ring of 16 cells at its far
end, mode 6 a perfect maze with many 2 x 2 blocks, mode 7 a random
4 x 4 maze with a random border entrance. Cycles of more than 16 cells
are then cut, as no snake of length 18 gets out."""

import random
import sys

H, W = 300, 30
LONGEST = 16
CORRIDOR = 20  # the last corridor column of mode 5
RING = 5  # the side of the ring of mode 5


def components(free, h, w, start):
    """Cell sets of the biconnected components reachable from start."""
    index, low = {start: 0}, {start: 0}
    stack, edges, out = [(start, -1, iter(neighbours(free, h, w, start)))], [], []
    while stack:
        v, parent, it = stack[-1]
        advanced = False
        for u in it:
            if u == parent:
                continue
            if u not in index:
                index[u] = low[u] = len(index)
                edges.append((v, u))
                stack.append((u, v, iter(neighbours(free, h, w, u))))
                advanced = True
                break
            if index[u] < index[v]:
                low[v] = min(low[v], index[u])
                edges.append((v, u))
        if advanced:
            continue
        stack.pop()
        if stack:
            p = stack[-1][0]
            low[p] = min(low[p], low[v])
            if low[v] >= index[p]:
                cells = set()
                while True:
                    a, b = edges.pop()
                    cells |= {a, b}
                    if (a, b) == (p, v):
                        break
                out.append(cells)
    return out


def neighbours(free, h, w, v):
    r, c = divmod(v, w)
    for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
        if 0 <= nr < h and 0 <= nc < w and free[nr * w + nc]:
            yield nr * w + nc


def perfect(rng, free, h, w):
    """A spanning tree maze on the cells with both coordinates even."""
    seen = {0}
    free[0] = True
    stack = [0]
    while stack:
        v = stack[-1]
        r, c = divmod(v, w)
        options = [
            (nr, nc)
            for nr, nc in ((r - 2, c), (r + 2, c), (r, c - 2), (r, c + 2))
            if 0 <= nr < h and 0 <= nc < w and nr * w + nc not in seen
        ]
        if not options:
            stack.pop()
            continue
        nr, nc = rng.choice(options)
        free[(r + nr) // 2 * w + (c + nc) // 2] = True
        free[nr * w + nc] = True
        seen.add(nr * w + nc)
        stack.append(nr * w + nc)


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    h, w = H, W
    free = [False] * (h * w)
    start = 0
    if mode == 7:
        h = w = 4
        share = rng.uniform(0.55, 0.95)
        free = [rng.random() < share for _ in range(h * w)]
        border = [r * w + c for r in range(h) for c in range(w)
                  if r in (0, h - 1) or c in (0, w - 1)]
        start = rng.choice(border)
    elif mode in (1, 2, 6):
        perfect(rng, free, h, w)
        blocks = {1: 0, 2: 150, 6: 600}[mode]
        for _ in range(blocks):
            r, c = rng.randrange(h - 1), rng.randrange(w - 1)
            if mode == 6:
                a = b = 2
            else:
                a, b = rng.randint(2, 6), rng.randint(2, 4)
            for i in range(a):
                for j in range(b):
                    if (i in (0, a - 1) or j in (0, b - 1)) and r + i < h and c + j < w:
                        free[(r + i) * w + c + j] = True
    elif mode in (3, 4):
        share = 0.6 if mode == 3 else 0.9
        free = [rng.random() < share for _ in range(h * w)]
        start = rng.randrange(w)
    else:
        # a corridor down and up the even columns up to 20, then a ring of 16 cells
        for c in range(0, CORRIDOR + 1, 2):
            for r in range(h):
                free[r * w + c] = True
            free[(h - 1 if c % 4 == 0 else 0) * w + c + 1] = True
        for r in range(h - RING, h):
            for c in range(CORRIDOR + 2, CORRIDOR + 2 + RING):
                if r in (h - RING, h - 1) or c in (CORRIDOR + 2, CORRIDOR + 1 + RING):
                    free[r * w + c] = True
    free[start] = True
    # cut every cycle of more than 16 cells
    while True:
        big = [cells for cells in components(free, h, w, start) if len(cells) > LONGEST]
        if not big:
            break
        for cells in big:
            for v in rng.sample(sorted(cells - {start}), max(1, len(cells) // LONGEST)):
                free[v] = False
    print(h, w)
    print(start // w + 1, start % w + 1)
    for r in range(h):
        print("".join("." if free[r * w + c] else "X" for c in range(w)))


main()
