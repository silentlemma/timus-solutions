"""Gold, limit and fee: a seed and a mode. Mode 1 draws any values, mode 2
a limit that the gold reaches exactly after some years."""

import random
import sys

TOP = 2**31 - 1


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        gold, limit, fee = rng.randint(1, TOP), rng.randint(1, TOP), rng.randint(1, 99)
    else:
        # the gold shrinks by fee/100 = (100 - keep) / 100 each year; pick
        # gold so that after some years it is a whole number
        keep = rng.choice([50, 75, 80, 90, 96])
        years = rng.randint(1, 4)
        gold = 100**years * rng.randint(1, TOP // 100**years)
        limit = gold * keep**years // 100**years
        fee = 100 - keep
    sys.stdout.write("%d %d %d\n" % (gold, limit, fee))


if __name__ == "__main__":
    main()
