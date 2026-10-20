"""A plane from a seed: mode 1 at most three rows with random free seats,
mode 2 100 rows with random free seats, mode 3 an empty plane with the
largest group that fits, mode 4 an empty plane with one person more."""

import random
import sys

MAX_N = 100
SMALL_N = 3
SIDE = 3


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    n = rng.randint(1, SMALL_N) if mode == 1 else MAX_N
    rows = []
    for _ in range(n):
        if mode <= 2:
            density = rng.random()
            seats = ["." if rng.random() < density else "*" for _ in range(2 * SIDE)]
        else:
            seats = ["."] * (2 * SIDE)
        rows.append("".join(seats[:SIDE]) + "|_|" + "".join(seats[SIDE:]))
    free = sum(row.count(".") for row in rows)
    if free == 0:
        rows[0] = "." + rows[0][1:]
        free = 1
    if mode <= 2:
        k = rng.randint(1, free)
    else:
        # two seats per side in every other row
        k = 2 * 2 * ((n + 1) // 2) + (mode - SIDE)
    print(n, k)
    print("\n".join(rows))


main()
