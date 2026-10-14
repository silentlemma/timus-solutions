"""One test from a seed and a mode: mode 1 a random cell of the board,
mode 2 a random reachable cell."""

import random
import sys

SIDE = 7
ARM = 2
LETTERS = "ABCDEFG"
REACHABLE = ["D4", "D1", "D7", "A4", "G4"]


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 2:
        print(rng.choice(REACHABLE))
        return
    cells = [
        "%s%d" % (LETTERS[c], r + 1)
        for r in range(SIDE)
        for c in range(SIDE)
        if ARM <= r < SIDE - ARM or ARM <= c < SIDE - ARM
    ]
    print(rng.choice(cells))


main()
