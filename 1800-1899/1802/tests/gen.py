"""One test from a seed and a mode. The cube is first cut by peeling
slabs off random sides of a shrinking box, each slab going to the part
on that side; then many times the last cell of a column is handed to
the part of another face whose column ends right next to it. Every part
is turned at random and the parts are shuffled. Mode 1 a small cube,
mode 2 a large one, mode 3 a small cube with one cell moved from one
part to another, mode 4 the same for a large cube, mode 5 a cube with
one part filling it all. Mode 6 assigns each cell to a nearest face,
breaking ties randomly; mode 7 distributes the required volume among
random columns without ensuring an assembly. Usage: seed mode [n],
where the optional side length applies only to modes 6 and 7 (default 20)."""

import random
import sys

FACES = 6
SMALL = 4
LARGE = 20
MOVES = 40


def face_cell(n, face, r, c, k):
    """The cell at depth k under row r, column c of a face."""
    last = n - 1
    cells = [(k, r, c), (last - k, last - r, c), (r, last - k, c),
             (r, k, last - c), (r, c, k), (r, last - c, last - k)]
    return cells[face]


def locate(n, face, cell):
    """Row, column and depth of a cell as seen from a face."""
    y, z, x = cell
    last = n - 1
    spots = [(z, x, y), (last - z, x, last - y), (y, x, last - z),
             (y, last - x, z), (y, z, x), (y, last - z, last - x)]
    return spots[face]


def cut(n, rng):
    heights = [[[0] * n for _ in range(n)] for _ in range(FACES)]
    low, high = [0, 0, 0], [n, n, n]  # the box left, axis by axis (y, z, x)
    while all(low[a] < high[a] for a in range(3)):
        face = rng.randrange(FACES)
        axis, from_low = [(0, True), (0, False), (1, False), (1, True), (2, True), (2, False)][face]
        thick = rng.randint(1, max(1, (high[axis] - low[axis]) // 2))
        for _ in range(thick):
            if low[axis] >= high[axis]:
                break
            depth = low[axis] if from_low else n - high[axis]
            ranges = [range(low[a], high[a]) for a in range(3)]
            ranges[axis] = [low[axis] if from_low else high[axis] - 1]
            for y in ranges[0]:
                for z in ranges[1]:
                    for x in ranges[2]:
                        r, c, k = locate(n, face, (y, z, x))
                        assert k == depth and heights[face][r][c] == depth
                        heights[face][r][c] += 1
            if from_low:
                low[axis] += 1
            else:
                high[axis] -= 1
    for _ in range(MOVES * n * n):
        a = rng.randrange(FACES)
        r, c = rng.randrange(n), rng.randrange(n)
        h = heights[a][r][c]
        if h == 0:
            continue
        cell = face_cell(n, a, r, c, h - 1)
        b = rng.randrange(FACES)
        rb, cb, kb = locate(n, b, cell)
        if b != a and heights[b][rb][cb] == kb:
            heights[a][r][c] -= 1
            heights[b][rb][cb] += 1
    return heights


def turn(grid):
    n = len(grid)
    return [[grid[n - 1 - c][r] for c in range(n)] for r in range(n)]


def nearest_faces(n, rng):
    """Each inward ray owns a prefix, even when distance ties are random."""
    owned = {}
    last = n - 1
    for y in range(n):
        for z in range(n):
            for x in range(n):
                depths = [y, last - y, last - z, z, x, last - x]
                closest = min(depths)
                owned[y, z, x] = rng.choice([f for f in range(FACES) if depths[f] == closest])
    heights = [[[0] * n for _ in range(n)] for _ in range(FACES)]
    for f in range(FACES):
        for r in range(n):
            for c in range(n):
                column = [owned[face_cell(n, f, r, c, k)] == f for k in range(n)]
                assert column == sorted(column, reverse=True)
                heights[f][r][c] = sum(column)
    return heights


def random_columns(n, rng):
    """Add exactly n cubed cells, keeping every column within its height limit."""
    heights = [[[0] * n for _ in range(n)] for _ in range(FACES)]
    for _ in range(n ** 3):
        while True:
            f, r, c = rng.randrange(FACES), rng.randrange(n), rng.randrange(n)
            if heights[f][r][c] < n:
                heights[f][r][c] += 1
                break
    return heights


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(2, SMALL) if mode in (1, 3) else rng.randint(LARGE - 5, LARGE)
    if mode in (6, 7):
        n = int(sys.argv[3]) if len(sys.argv) > 3 else LARGE
        if not 2 <= n <= LARGE:
            raise ValueError("side length must be between 2 and 20")
        parts = nearest_faces(n, rng) if mode == 6 else random_columns(n, rng)
    elif mode == 5:
        parts = [[[0] * n for _ in range(n)] for _ in range(FACES)]
        parts[0] = [[n] * n for _ in range(n)]
    else:
        parts = cut(n, rng)
    if mode in (3, 4):
        # move one cell from the top of one column to another column
        while True:
            a, b = rng.sample(range(FACES), 2)
            ra, ca, rb, cb = (rng.randrange(n) for _ in range(4))
            if parts[a][ra][ca] > 0 and parts[b][rb][cb] < n:
                parts[a][ra][ca] -= 1
                parts[b][rb][cb] += 1
                break
    for p in range(FACES):
        for _ in range(rng.randrange(4)):
            parts[p] = turn(parts[p])
    rng.shuffle(parts)
    lines = [str(n)]
    for part in parts:
        lines.extend(" ".join(map(str, row)) for row in part)
    print("\n".join(lines))


main()
