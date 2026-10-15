"""One test from a seed and a mode: a random grille with one window in
each group of four cells that turn into each other, its paper in one
piece, and a square of random letters; mode 2 uses only the letters a
and A, so that a wrong order still often looks plausible."""

import random
import string
import sys

SIZE = 4


def connected(grille):
    paper = [(r, c) for r in range(SIZE) for c in range(SIZE) if grille[r][c] == "."]
    seen = {paper[0]}
    stack = [paper[0]]
    while stack:
        r, c = stack.pop()
        for nr, nc in ((r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)):
            if (nr, nc) in paper and (nr, nc) not in seen:
                seen.add((nr, nc))
                stack.append((nr, nc))
    return len(seen) == len(paper)


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    half = SIZE // 2
    while True:
        grille = [["."] * SIZE for _ in range(SIZE)]
        for r in range(half):
            for c in range(half):
                # the four turns of the cell (r, c)
                cells = [(r, c), (c, SIZE - 1 - r), (SIZE - 1 - r, SIZE - 1 - c), (SIZE - 1 - c, r)]
                wr, wc = rng.choice(cells)
                grille[wr][wc] = "X"
        if connected(grille):
            break
    letters = "aA" if mode == 2 else string.ascii_letters
    for row in grille:
        print("".join(row))
    for _ in range(SIZE):
        print("".join(rng.choice(letters) for _ in range(SIZE)))


main()
