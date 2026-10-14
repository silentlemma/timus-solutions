"""One test from a seed and a mode. Mode 1 is 10000 random conductors and
50 friends, mode 2 all good conductors, mode 3 good conductors only at
places divisible by 10, mode 4 a few friends for many good conductors,
mode 5 a short line."""

import random
import sys

MOST = 10000
FRIENDS = 50
SHORT = 25


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(1, SHORT) if mode == 5 else MOST
    k = rng.randint(0, 3) if mode == 5 else FRIENDS
    if mode == 1:
        line = "".join(rng.choice("01") for _ in range(n))
    elif mode == 2:
        line = "1" * n
    elif mode == 3:
        line = "".join("1" if (i + 1) % 10 == 0 else "0" for i in range(n))
    elif mode == 4:
        k = rng.randint(1, 5)
        line = "".join("1" if rng.random() < 0.9 else "0" for _ in range(n))
    else:
        line = "".join(rng.choice("01") for _ in range(n))
    print(n, k)
    print(line)


main()
