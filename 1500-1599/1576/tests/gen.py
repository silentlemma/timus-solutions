"""One test from a seed and a mode: three tariffs and a list of calls.
Mode 1 has 1000 calls of any length, mode 2 many calls near the six
second and minute boundaries, mode 3 a few calls."""

import random
import sys

TOP = 1000
CALLS = 1000
FEW = 5


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    print(rng.randint(1, TOP), rng.randint(1, TOP))
    print(rng.randint(1, TOP), rng.randint(1, TOP), rng.randint(1, TOP))
    print(rng.randint(1, TOP))
    k = rng.randint(1, FEW) if mode == 3 else CALLS
    print(k)
    for _ in range(k):
        if mode == 2:
            mm = rng.choice([0, 0, rng.randint(0, 59)])
            ss = rng.choice([0, 1, 5, 6, 7, 59])
        else:
            mm, ss = rng.randint(0, 59), rng.randint(0, 59)
        print("%02d:%02d" % (mm, ss))


main()
