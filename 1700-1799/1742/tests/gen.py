"""One test from a seed and a mode: mode 1 up to 8 programmers, mode 2
100000 programmers pointing anywhere, mode 3 one cycle of 100000, mode
4 everyone thinks they are the strongest, mode 5 a long chain into a
small cycle."""

import random
import sys

FEW = 8
MOST = 100000
SMALL_CYCLE = 3


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n = rng.randint(1, FEW)
        to = [rng.randint(1, n) for _ in range(n)]
    elif mode == 2:
        n = MOST
        to = [rng.randint(1, n) for _ in range(n)]
    elif mode == 3:
        n = MOST
        order = list(range(1, n + 1))
        rng.shuffle(order)
        to = [0] * n
        for a, b in zip(order, order[1:] + order[:1]):
            to[a - 1] = b
    elif mode == 4:
        n = MOST
        to = list(range(1, n + 1))
    else:
        n = MOST
        to = [i + 2 for i in range(n)]
        to[-1] = n - SMALL_CYCLE + 1
    print(n)
    print("\n".join(map(str, to)))


main()
