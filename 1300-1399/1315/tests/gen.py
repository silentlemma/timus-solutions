"""A cave and a caver: a seed and a mode. Mode 1 gives a small random
cave, mode 2 a 500 x 500 random cave, mode 3 a 500 x 500 cave of air
pockets under a ceiling of rock with one shaft to the surface, mode 4 a
long winding tunnel under the surface, mode 5 an open 500 x 500 cave
with the caver at the bottom and D = 499 or 500, one short of the way
out or just enough. The caver always starts where the dry cave has a
way out, as the statement promises."""

import random
import sys
from collections import deque

SIDE = 500
REACH = 1000


def connected_to_top(rows):
    h, w = len(rows), len(rows[0])
    seen = set((0, c) for c in range(w) if rows[0][c] == ".")
    queue = deque(seen)
    while queue:
        r, c = queue.popleft()
        for nr, nc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            if 0 <= nr < h and 0 <= nc < w and rows[nr][nc] == "." and (nr, nc) not in seen:
                seen.add((nr, nc))
                queue.append((nr, nc))
    return sorted(seen)


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode in (1, 2):
        w, h = (rng.randint(1, 12), rng.randint(1, 12)) if mode == 1 else (SIDE, SIDE)
        share = rng.uniform(0.2, 0.45)
        rows = ["".join("#" if rng.random() < share else "." for _ in range(w)) for _ in range(h)]
        rows[0] = "." + rows[0][1:]
    elif mode == 3:
        w = h = SIDE
        grid = [["#"] * w for _ in range(h)]
        shaft = rng.randrange(1, w - 1)
        for r in range(h - 1):
            grid[r][shaft] = "."
        for c in range(1, w - 1):
            grid[h - 2][c] = "."
        # pockets hang above the bottom corridor, each one cell wide
        for c in range(1, w - 1, 2):
            if c != shaft:
                top = rng.randint(h - 2 - rng.randint(1, 40), h - 3)
                for r in range(top, h - 2):
                    grid[r][c] = "."
        rows = ["".join(row) for row in grid]
    else:
        w = h = SIDE
        grid = [["#"] * w for _ in range(h)]
        r, c = 0, rng.randrange(w)
        grid[0][c] = "."
        for _ in range(REACH * 3):
            dr, dc = rng.choice(((1, 0), (0, 1), (0, -1), (1, 0)))
            if 0 <= r + dr < h and 0 <= c + dc < w:
                r, c = r + dr, c + dc
                grid[r][c] = "."
        rows = ["".join(row) for row in grid]
    if mode == 5:
        print(SIDE, SIDE, SIDE // 2, 1, SIDE - 1 + seed % 2)
        print("\n".join("." * SIDE for _ in range(SIDE)))
        return
    cells = connected_to_top(rows)
    r, c = cells[-1] if mode == 4 else rng.choice(cells)
    d = rng.randint(1, 30 if mode == 1 else REACH)
    if mode == 3:
        d = rng.randint(SIDE - 5, SIDE + 5)  # about the climb up the shaft
    print(len(rows[0]), len(rows), c + 1, len(rows) - r, d)
    print("\n".join(rows))


main()
