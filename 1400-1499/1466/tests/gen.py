"""Seeded 9 by 9 inputs: bands SEED or symbol SEED.

bands chooses one random clue per block of a magic square.
symbol gives every occurrence of the largest number, in shuffled order.
"""

import random
import sys


def main():
    mode, seed = sys.argv[1:]
    if mode not in ("bands", "symbol"):
        raise ValueError("expected: bands SEED or symbol SEED")
    rng = random.Random(int(seed))
    labels = list(range(1, 9))
    rng.shuffle(labels)
    labels = [0] + labels
    row_offsets, col_offsets, block_rows, block_cols = [list(range(3)) for _ in range(4)]
    for offsets in (row_offsets, col_offsets, block_rows, block_cols):
        rng.shuffle(offsets)
    board = []
    for b in range(9):
        row = []
        for a in range(9):
            i, r = divmod(b, 3)
            j, c = divmod(a, 3)
            row.append(3 * ((row_offsets[r] + block_cols[j]) % 3)
                       + (col_offsets[c] + block_rows[i]) % 3)
        board.append(row)
    # Renaming the corner's original value to 0 preserves all distinctness rules.
    corner = board[0][0]
    labels[0], labels[corner] = labels[corner], labels[0]
    if mode == "bands":
        cells = [(3 * j + rng.randrange(3), 3 * i + rng.randrange(3))
                 for i in range(3) for j in range(3)]
    else:
        cells = [(a, b) for b in range(9) for a in range(9)
                 if labels[board[b][a]] == 8]
    rng.shuffle(cells)
    print(3, len(cells))
    for a, b in cells:
        print(a, b, labels[board[b][a]])


if __name__ == "__main__":
    main()
