"""A random journey: a seed and the depth F (0 picks it at random)."""

import random
import sys

TOP = 30


def main():
    seed, f = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    f = f or rng.randint(0, TOP)
    d, e = rng.randint(0, f), rng.randint(0, f)
    dp, ep = rng.randint(1, 2**f), rng.randint(1, 2**f)
    h = rng.randint(0, TOP)
    sys.stdout.write("%d %d %d %d %d %d\n" % (d, e, f, dp, ep, h))


if __name__ == "__main__":
    main()
