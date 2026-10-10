"""A board with three crosses and three noughts and no full line: a
seed picks it at random."""

import random
import sys

LINES = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
CELLS = 9
EACH = 3
SIDE = 3


def main():
    rng = random.Random(int(sys.argv[1]))
    while True:
        cells = rng.sample(range(CELLS), 2 * EACH)
        board = ["#"] * CELLS
        for k, i in enumerate(cells):
            board[i] = "X" if k < EACH else "O"
        if not any(all(board[i] == m for i in line) for line in LINES for m in "XO"):
            break
    rows = ["".join(board[r * SIDE : (r + 1) * SIDE]) for r in range(SIDE)]
    sys.stdout.write("\n".join(rows) + "\n")


if __name__ == "__main__":
    main()
