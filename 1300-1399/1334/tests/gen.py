"""A game of 32 moves on all the dark squares: a seed and a mode. Mode 1
gives a random order, mode 2 white filling the lower half and black the
upper half with a few squares swapped, mode 3 the same game with more
swaps."""

import random
import sys

SIZE = 8
HALF = SIZE // 2


def dark(row):
    return [chr(ord("a") + c) + str(row + 1) for c in range(SIZE) if (c + row) % 2 == 0]


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    white = [s for r in range(HALF) for s in dark(r)]
    black = [s for r in range(SIZE - 1, HALF - 1, -1) for s in dark(r)]
    if mode == 1:
        squares = white + black
        rng.shuffle(squares)
        white, black = squares[::2], squares[1::2]
    else:
        for _ in range(2 if mode == 2 else 6):
            i, j = rng.randrange(len(white)), rng.randrange(len(white))
            white[i], white[j] = white[j], white[i]
            i, j = rng.randrange(len(black)), rng.randrange(len(black))
            black[i], black[j] = black[j], black[i]
    for w, b in zip(white, black):
        print(w)
        print(b)


main()
