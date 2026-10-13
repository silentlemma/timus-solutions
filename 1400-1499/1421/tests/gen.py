"""Credit sums for 100 firms and banks: a seed and a mode. Modes 1 and 2
take the sums of a random matrix (credits from 0 to 100, then from 90 to
100), so a matrix exists; mode 3 moves one unit of a full matrix's row
sums so that a row needs 10 001; mode 4 is the matrix of all 100s."""

import random
import sys

N = 100
CAP = 100


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        matrix = [[rng.randint(0, CAP) for _ in range(N)] for _ in range(N)]
    elif mode == 2:
        matrix = [[rng.randint(CAP - 10, CAP) for _ in range(N)] for _ in range(N)]
    else:
        matrix = [[CAP] * N for _ in range(N)]
    rows = [sum(r) for r in matrix]
    cols = [sum(matrix[i][j] for i in range(N)) for j in range(N)]
    if mode == 3:
        rows[0] += 1
        rows[1] -= 1
    print(N)
    print(" ".join(map(str, rows)))
    print(" ".join(map(str, cols)))


main()
