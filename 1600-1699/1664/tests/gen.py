"""One test from a seed and a mode: a grid of stations with one diagonal
per cell and some pipes removed, plus the source far to the left joined
to the left column and the sink far to the right joined to the right
column. Mode 1 is small, mode 2 has about 10000 stations, mode 3 a long
thin strip as wide as the coordinates allow, mode 4 a medium grid with
large capacities, mode 5 the full grid of mode 2 with every pipe.
Mode 6 is a 10000-station zigzag chain with shuffled pipes; mode 7 has
20 independent two-pipe routes, attaining flow 2*10^9; mode 8 is a
randomly weighted convex polygon triangulated from a random pivot.
Arguments: seed mode [size]; size is optional only for mode 8 (default 160)."""

import random
import sys

FAR = 10 ** 8
STRIP = 9 * 10 ** 7
MOST_CAP = 10 ** 8
LIMIT = 2 * 10 ** 9
KEEP = 0.85


def special(rng, mode):
    if mode == 6:
        count = 10000
        pts = [(-FAR + 20000 * i, FAR if i % 2 else -FAR) for i in range(count)]
        edges = [(i, i + 1, 17 if i == count // 2 else MOST_CAP)
                 for i in range(1, count)]
    elif mode == 7:
        pts = [(-FAR, 0)] + [(0, 1000 * i - 9500) for i in range(20)] + [(FAR, 0)]
        edges = [(a, b, MOST_CAP) for i in range(2, 22) for a, b in ((1, i), (i, 22))]
    else:
        count = int(sys.argv[3]) if len(sys.argv) > 3 else 160
        if not 3 <= count <= 1000:
            raise ValueError("mode 8 size must be from 3 to 1000")
        pts = [(1000 * (i - count // 2), 100 * (i - count // 2) ** 2)
               for i in range(count)]
        pivot = rng.randrange(2, count)
        pairs = {(i, i + 1) for i in range(1, count)} | {(1, count)}
        pairs |= {tuple(sorted((pivot, i))) for i in range(1, count + 1) if i != pivot}
        edges = [(a, b, rng.choice((1, MOST_CAP, rng.randint(2, 1000))))
                 for a, b in sorted(pairs)]
    rng.shuffle(edges)
    print(len(pts))
    for x, y in pts:
        print(x, y)
    print(len(edges))
    for a, b, cap in edges:
        if rng.randrange(2):
            a, b = b, a
        print(a, b, cap)


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode in (6, 7, 8):
        special(rng, mode)
        return
    rows, cols = {1: (3, 4), 2: (100, 99), 3: (3, 3300), 4: (40, 40), 5: (100, 99)}[mode]
    keep = 1.0 if mode == 5 else KEEP
    cell = 2 * STRIP // cols if mode == 3 else 1000
    left = -STRIP if mode == 3 else 0
    jitter = cell // 10
    top_cap = MOST_CAP if mode in (3, 4) else 100
    middle = rows // 2
    # the source, the grid row by row, the sink
    pts = [(-FAR, middle * cell)]
    for r in range(rows):
        for c in range(cols):
            pts.append((left + c * cell + rng.randint(-jitter, jitter),
                        r * cell + rng.randint(-jitter, jitter)))
    pts.append((FAR, middle * cell))
    sink = len(pts)

    def at(r, c):
        return 2 + r * cols + c

    pipes = []
    for r in range(rows):
        for c in range(cols):
            if c + 1 < cols and (r == middle or rng.random() < keep):
                pipes.append((at(r, c), at(r, c + 1)))
            if r + 1 < rows and rng.random() < keep:
                pipes.append((at(r, c), at(r + 1, c)))
            if r + 1 < rows and c + 1 < cols and rng.random() < keep:
                if rng.random() < 0.5:
                    pipes.append((at(r, c), at(r + 1, c + 1)))
                else:
                    pipes.append((at(r, c + 1), at(r + 1, c)))
    pipes += [(1, at(r, 0)) for r in range(rows)]
    pipes += [(at(r, cols - 1), sink) for r in range(rows)]
    rng.shuffle(pipes)
    # keep the total flow within 2 * 10^9 by limiting the source pipes
    source_cap = LIMIT // rows
    lines = []
    for a, b in pipes:
        cap = rng.randint(1, top_cap)
        if a == 1 or b == 1:
            cap = min(cap, source_cap)
        if rng.random() < 0.5:
            a, b = b, a
        lines.append("%d %d %d" % (a, b, cap))
    print(len(pts))
    for x, y in pts:
        print(x, y)
    print(len(lines))
    print("\n".join(lines))


main()
