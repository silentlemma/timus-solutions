"""N and K: a seed and a mode. Mode 1 draws both below 10000; mode 2 makes
N mod K just under K / 2, mode 3 just over, the two sides of the switch
between leftover r and K - r."""

import random
import sys

TOP = 9999


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n, k = rng.randint(2, TOP), rng.randint(2, TOP)
    else:
        k = rng.randint(4, TOP // 4)
        half = k // 2
        r = half if mode == 2 else half + 1
        n = k * rng.randint(1, TOP // k - 1) + r
    sys.stdout.write("%d %d\n" % (n, k))


if __name__ == "__main__":
    main()
