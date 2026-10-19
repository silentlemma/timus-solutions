"""Road lengths from a seed: mode 1 a few small ones, mode 2 10^5 random ones,
mode 3 10^5 roads of the largest length, mode 4 10^5 roads of length one,
mode 5 99999 shuffled endpoint lengths with an odd total."""

import random
import sys

MAX_N = 10 ** 5
MAX_D = 10 ** 4
SMALL = 10


def main():
    mode, seed = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    if mode == 1:
        d = [rng.randint(1, SMALL) for _ in range(rng.randint(1, SMALL))]
    elif mode == 2:
        d = [rng.randint(1, MAX_D) for _ in range(MAX_N)]
    elif mode == 4:
        d = [1] * MAX_N
    elif mode == 5:
        d = [1]
        for _ in range((MAX_N - 2) // 2):
            length = rng.choice((1, MAX_D))
            d.extend((length, length))
        rng.shuffle(d)
    else:
        d = [MAX_D] * MAX_N
    print(len(d))
    print(*d)


main()
