"""Tables of 100 fingers: a seed and a mode. Mode 1 has random
consolation prizes from 0 to 10, mode 2 only 0 and 10, mode 3 gives 10
for a single row and 0 elsewhere, mode 4 gives prizes that grow with
the player's fingers."""

import random
import sys

N = 100
JACKPOT = 1000
TOP = 10


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    rows = []
    for i in range(N):
        if mode == 1:
            row = [rng.randint(0, TOP) for _ in range(N)]
        elif mode == 2:
            row = [rng.choice((0, TOP)) for _ in range(N)]
        elif mode == 3:
            row = [TOP if i == N // 2 else 0 for _ in range(N)]
        else:
            row = [i * TOP // N for _ in range(N)]
        row[i] = JACKPOT
        rows.append(" ".join(map(str, row)))
    print(N)
    print("\n".join(rows))


main()
