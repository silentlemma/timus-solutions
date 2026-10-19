"""n and k from a seed and a mode: 1 small random, 2 k = n, 3 k = 1, 4 the
largest n with random k, 5 the largest n with k = n, 6 the largest n with
an even k."""

import random
import sys

MOST = 500


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(1, 20) if mode <= 3 else MOST
    if mode in (2, 5):
        k = n
    elif mode == 3:
        k = 1
    elif mode == 6:
        k = rng.randrange(2, n + 1, 2)
    else:
        k = rng.randint(1, n)
    print(n, k)


main()
