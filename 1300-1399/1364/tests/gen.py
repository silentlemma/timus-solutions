"""A cemetery and Lara's place: a seed and a mode. Mode 1 gives a full
100 x 100 spiral with Lara at the entrance and the longest time, mode 2
a random cemetery with random places on the tunnel, mode 3 Lara at the
treasure in the middle of a full 100 x 100 spiral. Mode 4 gives a 99 x 100
spiral with a long reachable window strictly inside the tunnel; mode 5
gives a 100 x 100 spiral with Lara shortly before a deep, early treasure
and enough time to run beyond it if the tunnel were not truncated."""

import random
import sys

STEPS = ((0, 1), (1, 0), (0, -1), (-1, 0))
SIDE = 100
LONGEST = 27000


def spiral(n, m):
    seen = [[False] * m for _ in range(n)]
    path, r, c, d = [(0, 0)], 0, 0, 0
    seen[0][0] = True
    while len(path) < n * m:
        dr, dc = STEPS[d]
        nr, nc = r + dr, c + dc
        if not (0 <= nr < n and 0 <= nc < m) or seen[nr][nc]:
            d = (d + 1) % len(STEPS)
            continue
        r, c = nr, nc
        seen[r][c] = True
        path.append((r, c))
    return path


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    n, m = (SIDE, SIDE) if mode != 2 else (rng.randint(2, SIDE), rng.randint(2, SIDE))
    if mode == 4:
        n = SIDE - 1
    path = spiral(n, m)
    if mode == 1:
        treasure, lara, t = len(path) - 1, 0, LONGEST
    elif mode == 2:
        treasure = rng.randrange(len(path))
        lara, t = rng.randint(0, treasure), rng.randint(0, 3 * SIDE)
    elif mode == 4:
        treasure = rng.randint(8500, len(path) - 1)
        lara, t = rng.randint(4950, 5940), rng.randint(1500, 2000)
    elif mode == 5:
        treasure = rng.randint(9000, 9500)
        lara, t = treasure - rng.randint(10, 20), rng.randint(40, 60)
    else:
        treasure = lara = len(path) - 1
        t = SIDE // 2
    print(n, m)
    print(path[treasure][0] + 1, path[treasure][1] + 1)
    print(path[lara][0] + 1, path[lara][1] + 1)
    print(t)


main()
