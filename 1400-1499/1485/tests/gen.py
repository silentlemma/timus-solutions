"""One test from a seed and a mode. Mode 1 is a small random matrix,
mode 2 has 100 captains speaking about nearly everyone (often no answer),
mode 3 takes a real tournament and real liars, so an answer exists,
mode 4 has 100 captains who rarely speak."""

import random
import sys

LARGEST = 100
SMALL = 8
OFTEN, RARELY = 0.95, 0.05
WIN, DRAW = 3, 1


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(1, SMALL) if mode == 1 else LARGEST
    chance = {1: rng.random(), 2: OFTEN, 3: rng.random(), 4: RARELY}[mode]
    said = [[-1] * n for _ in range(n)]
    if mode == 3:
        table = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                table[i][j], table[j][i] = rng.choice([(WIN, 0), (0, WIN), (DRAW, DRAW)])
        liar = [rng.random() < 0.5 for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i != j and rng.random() < chance:
                    said[i][j] = int((table[i][j] > 0) != liar[i])
    else:
        for i in range(n):
            for j in range(n):
                if i != j and rng.random() < chance:
                    said[i][j] = rng.randint(0, 1)
    print(n)
    for row in said:
        print(" ".join(map(str, row)))


main()
