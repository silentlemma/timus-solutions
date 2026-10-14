"""One test from a seed and a mode: mode 1 a random n up to 100, mode 2 a
random even n, mode 3 a random odd n, mode 4 the largest n, mode 5 the
largest odd n."""

import random
import sys

MOST = 100


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n = rng.randint(1, MOST)
    elif mode == 2:
        n = rng.randrange(2, MOST + 1, 2)
    elif mode == 3:
        n = rng.randrange(1, MOST, 2)
    elif mode == 4:
        n = MOST
    else:
        n = MOST - 1
    print(n)


main()
