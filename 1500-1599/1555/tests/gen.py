"""A maze from a seed and a mode. Mode 1 is a small board with a few walls,
mode 2 a 6 x 6 board with 30 walls, mode 3 a 6 x 6 board without walls,
mode 4 a 6 x 6 board with walls only on the border, mode 5 a board of
random size with the chest next to the second player."""

import random
import sys

MOST_WALLS = 30
LARGEST = 6
CELL = 3
SIDES = 4
# where the wall of each side is drawn inside the 3 x 3 square, and its character
SPOTS = [(0, 1, "-"), (1, 2, "|"), (2, 1, "-"), (1, 0, "|")]


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(2, 3) if mode == 1 else rng.randint(2, LARGEST) if mode == 5 else LARGEST
    rows = [[" "] * (CELL * n) for _ in range(CELL * n)]
    spots = [(r, c, d) for r in range(n) for c in range(n) for d in range(SIDES)]
    if mode == 4:
        spots = [
            (r, c, d)
            for r, c, d in spots
            if (d == 0 and r == 0) or (d == 2 and r == n - 1) or (d == 3 and c == 0) or (d == 1 and c == n - 1)
        ]
    count = {1: rng.randint(0, 6), 2: MOST_WALLS, 3: 0, 4: rng.randint(4, 12)}.get(mode, rng.randint(0, 12))
    for r, c, d in rng.sample(spots, min(count, len(spots))):
        dr, dc, ch = SPOTS[d]
        rows[CELL * r + dr][CELL * c + dc] = ch
    places = rng.sample(range(n * n), 3)
    if mode == 5:
        second = places[1]
        near = [x for x in range(n * n) if abs(x // n - second // n) + abs(x % n - second % n) == 1]
        near = [x for x in near if x != places[0]]
        places[2] = rng.choice(near)
    for mark, place in zip("12*", places):
        rows[CELL * (place // n) + 1][CELL * (place % n) + 1] = mark
    print(n)
    print("\n".join("".join(r) for r in rows))


main()
