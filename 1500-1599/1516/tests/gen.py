"""One test from a seed and a mode: between 1 and 12 checkers of each colour
on the dark squares. Mode 1 places them at random, mode 2 puts 12 blacks
inside the board with gaps between them, so that long captures exist,
mode 3 places only a few checkers, mode 4 puts the blacks on the edge,
where nothing can capture them."""

import random
import sys

SIZE = 8
MOST = 12
FEW = 3


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    dark = [(x, y) for x in range(SIZE) for y in range(SIZE) if (x + y) % 2 == 0]
    edge = [(x, y) for x, y in dark if x in (0, SIZE - 1) or y in (0, SIZE - 1)]
    inner = [(x, y) for x, y in dark if (x, y) not in edge]
    if mode == 2:
        # every other inner diagonal square, so the squares between are free
        spots = [(x, y) for x, y in inner if x % 2 == 1]
        blacks = rng.sample(spots, min(MOST, len(spots)))
        whites = rng.sample([s for s in dark if s not in blacks], rng.randint(1, MOST))
    elif mode == 4:
        blacks = rng.sample(edge, rng.randint(1, MOST))
        whites = rng.sample([s for s in dark if s not in blacks], rng.randint(1, MOST))
    else:
        top = FEW if mode == 3 else MOST
        cells = rng.sample(dark, rng.randint(1, top) + rng.randint(1, top))
        split = rng.randint(1, len(cells) - 1)
        whites, blacks = cells[:split], cells[split:]
        whites, blacks = whites[:MOST], blacks[:MOST]
    board = [["."] * SIZE for _ in range(SIZE)]
    for x, y in whites:
        board[SIZE - 1 - y][x] = "W"
    for x, y in blacks:
        board[SIZE - 1 - y][x] = "B"
    print("\n".join("".join(row) for row in board))


main()
