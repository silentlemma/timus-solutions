"""Tables of 100 fingers: a seed and a mode.

Mode 1: random prizes from 0 to 10. Mode 2: only 0 and 10.
Mode 3: 10 for a single row and 0 elsewhere.
Mode 4: prizes growing with the player's fingers.
Mode 5: unequal groups of 30 and 70, with cross prizes 10 and 1.
Mode 6: dense random prizes of 9 or 10.
Mode 7: sparse symmetric random prizes, with unequal weighted degrees.
Mode 8: a directed circular band of five random positive prizes per row.
"""

import random
import sys

N = 100
JACKPOT = 1000
TOP = 10


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 7:
        matrix = [[0] * N for _ in range(N)]
        for i in range(N):
            for j in range(i + 1, N):
                if rng.randrange(8) == 0:
                    matrix[i][j] = matrix[j][i] = rng.randint(1, TOP)
    rows = []
    for i in range(N):
        if mode == 1:
            row = [rng.randint(0, TOP) for _ in range(N)]
        elif mode == 2:
            row = [rng.choice((0, TOP)) for _ in range(N)]
        elif mode == 3:
            row = [TOP if i == N // 2 else 0 for _ in range(N)]
        elif mode == 5:
            row = [TOP if i < 30 <= j else 1 if j < 30 <= i else 0 for j in range(N)]
        elif mode == 6:
            row = [rng.choice((TOP - 1, TOP)) for _ in range(N)]
        elif mode == 7:
            row = matrix[i][:]
        elif mode == 8:
            row = [0] * N
            for offset in range(1, 6):
                row[(i + offset) % N] = rng.randint(1, TOP)
        else:
            row = [i * TOP // N for _ in range(N)]
        row[i] = JACKPOT
        rows.append(" ".join(map(str, row)))
    print(N)
    print("\n".join(rows))


main()
