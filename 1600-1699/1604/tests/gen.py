"""One test from a seed and a mode, with at most 10000 signs. Mode 1 has
random counts, mode 2 one kind with more than half the signs, mode 3
10000 kinds of one sign each, mode 4 one kind with exactly half, mode 5 a
few kinds with similar counts."""

import random
import sys

MOST = 10000


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        counts = []
        while sum(counts) < MOST - 100:
            counts.append(rng.randint(1, 100))
    elif mode == 2:
        big = rng.randint(MOST // 2 + 1, MOST - 1)
        counts = [big]
        while sum(counts) < MOST:
            counts.append(rng.randint(1, min(50, MOST - sum(counts))))
        rng.shuffle(counts)
    elif mode == 3:
        counts = [1] * MOST
    elif mode == 4:
        counts = [MOST // 2] + [1] * (MOST // 2)
        rng.shuffle(counts)
    else:
        counts = [rng.randint(2000, 2400) for _ in range(4)]
    print(len(counts))
    print(*counts)


main()
