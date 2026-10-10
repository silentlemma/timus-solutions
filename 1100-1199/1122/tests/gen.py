"""Random games: a seed, a mode and a pattern ("random" or nine 0/1
digits). Mode 0 draws any board, mode 1 builds a solvable one by playing
random moves from a board of one colour."""

import random
import sys

SIZE = 4
PATTERN = 3


def main():
    seed, mode, spec = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    rng = random.Random(seed)
    if spec == "random":
        spec = "".join(rng.choice("01") for _ in range(PATTERN * PATTERN))
    pattern = [spec[i : i + PATTERN] for i in range(0, PATTERN * PATTERN, PATTERN)]
    if mode == 1:
        colour = rng.choice("WB")
        board = [[colour] * SIZE for _ in range(SIZE)]
        flip = {"W": "B", "B": "W"}
        for _ in range(rng.randint(1, SIZE * SIZE)):
            r, c = rng.randrange(SIZE), rng.randrange(SIZE)
            for dr in range(PATTERN):
                for dc in range(PATTERN):
                    rr, cc = r + dr - 1, c + dc - 1
                    if pattern[dr][dc] == "1" and 0 <= rr < SIZE and 0 <= cc < SIZE:
                        board[rr][cc] = flip[board[rr][cc]]
    else:
        board = [[rng.choice("WB") for _ in range(SIZE)] for _ in range(SIZE)]
    sys.stdout.write("\n".join(["".join(row) for row in board] + pattern) + "\n")


if __name__ == "__main__":
    main()
