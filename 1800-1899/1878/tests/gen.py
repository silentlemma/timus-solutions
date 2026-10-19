"""A cube state from a seed and a mode: every layer holds the four
squares of one orbit of the quarter turn, and the quadrants of a solved
cube get the colours in a random order. Mode 1 turns every layer at
random, 2 turns at most one layer, 3 turns every layer by a half turn
or not at all, 4 leaves the cube solved but turned as a whole."""

import random
import sys

SIDE = 4
TURNS = 4
HALF = SIDE // 2


def turn(r, c, times):
    for _ in range(times):
        r, c = c, SIDE - 1 - r
    return r, c


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    colours = list(range(1, TURNS + 1))
    rng.shuffle(colours)
    # the solved cube: the quadrant of the cell decides its colour
    solved = [[colours[(r // HALF) * 2 + c // HALF] for c in range(SIDE)] for r in range(SIDE)]
    whole = rng.randrange(TURNS)
    grid = [[0] * SIDE for _ in range(SIDE)]
    moved = rng.randrange(HALF * HALF)
    for layer, (r0, c0) in enumerate((r, c) for r in range(HALF) for c in range(HALF)):
        if mode == 1:
            k = rng.randrange(TURNS)
        elif mode == 2:
            k = rng.randrange(TURNS) if layer == moved else 0
        elif mode == 3:
            k = rng.choice([0, 2])
        else:
            k = 0
        for times in range(TURNS):
            r, c = turn(r0, c0, times)
            nr, nc = turn(r, c, k + whole)
            grid[nr][nc] = solved[r][c]
    print("\n".join(" ".join(map(str, row)) for row in grid))


main()
