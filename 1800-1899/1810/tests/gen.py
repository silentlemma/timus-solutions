"""One test from a seed and a mode: k antiequations in n variables with
coefficients mod 3. Mode 1 small k and n, mode 2 k = n = 30 with any
coefficients, mode 3 k = 30 rows spanning only a few dimensions, mode 4
many rows that are copies or multiples of a few, mode 5 few variables
and 30 rows."""

import random
import sys

MOD = 3
LIMIT = 30
SMALL = 6


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)

    def rand_row(width):
        return [rng.randrange(MOD) for _ in range(width)]

    if mode == 1:
        k, n = rng.randint(1, SMALL), rng.randint(1, SMALL)
        a = [rand_row(n) for _ in range(k)]
    elif mode == 2:
        k, n = LIMIT, LIMIT
        a = [rand_row(n) for _ in range(k)]
    elif mode in (3, 4):
        k, n = LIMIT, rng.randint(1, LIMIT)
        base = [rand_row(n) for _ in range(rng.randint(1, SMALL))]
        a = []
        for _ in range(k):
            if mode == 3:
                row = [0] * n
                for vec in base:
                    c = rng.randrange(MOD)
                    row = [(x + c * y) % MOD for x, y in zip(row, vec)]
            else:
                c = rng.randint(1, MOD - 1)
                row = [c * y % MOD for y in rng.choice(base)]
            a.append(row)
    else:
        k, n = LIMIT, rng.randint(1, SMALL)
        a = [rand_row(n) for _ in range(k)]
    print(k, n)
    for row in a:
        print(*(row + [rng.randrange(MOD)]))


main()
