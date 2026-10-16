"""One test from a seed and a mode: k antiequations in n variables with
coefficients mod 3. Mode 1 small k and n, mode 2 k = n = 30 with any
coefficients, mode 3 k = 30 rows spanning only a few dimensions, mode 4
many rows that are copies or multiples of a few, mode 5 few variables
and 30 rows, mode 6 ten satisfiable dependent three-variable blocks at
k = n = 30, mode 7 a randomly relabelled cycle at k = n = 30."""

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
    elif mode == 6:
        k, n = LIMIT, LIMIT
        a, targets = [], []
        for start in range(0, n, 3):
            first = [rng.randint(1, 2) for _ in range(3)]
            second = [rng.randint(1, 2) for _ in range(3)]
            while second == first or second == [2 * x % MOD for x in first]:
                second = [rng.randint(1, 2) for _ in range(3)]
            third = [(x + 2 * y) % MOD for x, y in zip(first, second)]
            witness = rand_row(3)
            for block in (first, second, third):
                a.append([0] * start + block + [0] * (n - start - 3))
                value = sum(x * y for x, y in zip(block, witness)) % MOD
                targets.append((value + rng.randint(1, 2)) % MOD)
    elif mode == 7:
        k, n = LIMIT, LIMIT
        a, targets = [], []
        for i in range(n):
            row = [0] * n
            row[i] = rng.randint(1, 2)
            row[(i + 1) % n] = -row[i] % MOD
            a.append(row)
            targets.append(rng.randrange(MOD))
    else:
        k, n = LIMIT, rng.randint(1, SMALL)
        a = [rand_row(n) for _ in range(k)]
    if mode in (6, 7):
        columns = list(range(n))
        rng.shuffle(columns)
        order = list(range(k))
        rng.shuffle(order)
        print(k, n)
        for i in order:
            print(*[a[i][j] for j in columns], targets[i])
        return
    print(k, n)
    for row in a:
        print(*(row + [rng.randrange(MOD)]))


main()
