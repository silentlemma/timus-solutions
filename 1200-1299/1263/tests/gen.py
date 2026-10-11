"""N, M and the votes: a seed and a mode. Mode 1 draws everything at
random, mode 2 takes M = 2^a * 5^b so that some shares end in an exact
half of the last printed digit."""

import random
import sys

TOP = 10000


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n, m = rng.randint(1, TOP), rng.randint(1, TOP)
    else:
        n = rng.randint(1, 50)
        m = rng.choice([2**a * 5**b for a in range(14) for b in range(6) if 2**a * 5**b <= TOP])
    votes = [rng.randint(1, n) for _ in range(m)]
    sys.stdout.write("%d %d\n%s" % (n, m, "".join("%d\n" % v for v in votes)))


if __name__ == "__main__":
    main()
