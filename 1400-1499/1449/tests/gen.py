"""Credit matrices: a seed, N and a mode. Mode 1 draws every credit up to
a million, mode 2 builds A[i][j] = r[i] + c[j] (the bribes can match
every credit exactly), mode 3 uses values 0 and 1 only. Mode 4 draws
credits from 999998 through 1000000. Mode 5 makes a lower triangle of
million-valued credits with zeros above it. Mode 6 plants a tight perfect
matching in random row/column sums and subtracts random slack elsewhere."""

import random
import sys

TOP = 10**6


def main():
    seed, n, mode = (int(a) for a in sys.argv[1:4])
    rng = random.Random(seed)
    if mode == 1:
        a = [[rng.randint(0, TOP) for _ in range(n)] for _ in range(n)]
    elif mode == 2:
        r = [rng.randint(0, TOP // 2) for _ in range(n)]
        c = [rng.randint(0, TOP // 2) for _ in range(n)]
        a = [[r[i] + c[j] for j in range(n)] for i in range(n)]
    elif mode == 4:
        a = [[TOP - rng.randint(0, 2) for _ in range(n)] for _ in range(n)]
    elif mode == 5:
        a = [[TOP if j <= i else 0 for j in range(n)] for i in range(n)]
    elif mode == 6:
        r = [rng.randint(0, TOP // 2) for _ in range(n)]
        c = [rng.randint(0, TOP // 2) for _ in range(n)]
        r[0], r[-1] = 0, TOP // 2
        c[0], c[-1] = 0, TOP // 2
        matching = list(range(n - 1))
        rng.shuffle(matching)
        matching.append(n - 1)
        a = [
            [
                r[i] + c[j]
                if j == matching[i]
                else max(0, r[i] + c[j] - rng.randint(1, TOP))
                for j in range(n)
            ]
            for i in range(n)
        ]
    else:
        a = [[rng.randint(0, 1) for _ in range(n)] for _ in range(n)]
    print(n)
    print("\n".join(" ".join(map(str, row)) for row in a))


main()
