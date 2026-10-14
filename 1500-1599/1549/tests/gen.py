"""One test from a seed and a mode: mode 1 takes random S and T up to
1000, mode 2 values up to 20, mode 3 at most one straight, mode 4 T that
leaves 2 modulo 4."""

import random
import sys

TOP = 1000
SMALL = 20


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    top = SMALL if mode == 2 else TOP
    s, t = rng.randint(0, top), rng.randint(0, top)
    if mode == 3:
        s = rng.randint(0, 1)
    if mode == 4:
        t -= t % 4
        t += 2
    if s + t == 0:
        t = 1
    print(s, t)


main()
