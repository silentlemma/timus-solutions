"""One test from a seed and a mode: a timetable that a renumbering can
mend, built from a hidden order and then shuffled; mode 1 up to 6 rooms,
mode 2 100 rooms with sparse use, mode 3 100 rooms with dense use, mode
4 like mode 2 with one use that closes a cycle, so nothing helps;
mode 5 has 100 rooms in two independent layers with random uses between
them and all diagonal entries set; mode 6 has an 80-room chain feeding
a 20-room cycle, plus random forward uses within the chain."""

import random
import sys

FEW = 6
MOST = 100
SPARSE = 0.1
DENSE = 0.8


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode in (5, 6):
        grid = [[0] * MOST for _ in range(MOST)]
        if mode == 5:
            for i in range(MOST):
                grid[i][i] = 1
            for i in range(MOST // 2):
                for j in range(MOST // 2, MOST):
                    grid[i][j] = int(rng.random() < 0.5)
        else:
            prefix = 80
            for i in range(MOST):
                grid[i][i] = rng.randint(0, 1)
                if i + 1 < MOST:
                    grid[i][i + 1] = 1
            grid[MOST - 1][prefix] = 1
            for i in range(prefix):
                for j in range(i + 2, prefix):
                    grid[i][j] = int(rng.random() < SPARSE)
        shuffle = list(range(MOST))
        rng.shuffle(shuffle)
        print(MOST)
        for i in shuffle:
            print(" ".join(str(grid[i][j]) for j in shuffle))
        return
    n = rng.randint(2, FEW) if mode == 1 else MOST
    chance = DENSE if mode == 3 else (rng.random() if mode == 1 else SPARSE)
    # in the hidden order a contest only uses its own room and later ones
    grid = [[1 if j > i and rng.random() < chance else 0 for j in range(n)] for i in range(n)]
    for i in range(n):
        grid[i][i] = rng.randint(0, 1)
    if mode == 4:
        i, j = sorted(rng.sample(range(n), 2))
        grid[i][j] = 1
        grid[j][i] = 1
    shuffle = list(range(n))
    rng.shuffle(shuffle)
    print(n)
    for i in range(n):
        print(" ".join(str(grid[shuffle[i]][shuffle[j]]) for j in range(n)))


main()
