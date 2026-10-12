"""10000 readings and 100000 questions: a seed and a mode. Mode 1 gives
random readings, mode 2 every reading 10000 or every reading -10000,
mode 3 long questions only."""

import random
import sys

N = 10000
Q = 100000
TOP = 10000


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 2:
        readings = [rng.choice([TOP, -TOP])] * N
    else:
        readings = [rng.randint(-TOP, TOP) for _ in range(N)]
    print(N)
    print("\n".join(map(str, readings)))
    print(Q)
    for _ in range(Q):
        if mode == 3:
            i, j = rng.randint(1, N // 10), rng.randint(N - N // 10, N)
        else:
            i, j = sorted((rng.randint(1, N), rng.randint(1, N)))
        print(i, j)


main()
