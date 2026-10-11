"""K: a seed and a mode. Mode 1 draws any K up to 10^9, mode 2 a K with
many one bits (the longest programs)."""

import random
import sys

TOP = 10**9


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        k = rng.randint(1, TOP)
    else:
        bits = rng.randint(2, 29)
        k = (1 << bits) - 1 - rng.choice([0, 1 << rng.randrange(bits)])
    sys.stdout.write("%d\n" % max(k, 1))


if __name__ == "__main__":
    main()
