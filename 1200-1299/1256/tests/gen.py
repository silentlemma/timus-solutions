"""R1, R2, R3 and the chain: a seed and a mode. The three distances always
make a triangle (possibly flat). Mode 1 draws short chains, mode 2 chains
comparable to the distances, mode 3 posts far apart with the house between
them."""

import random
import sys

TOP = 20000


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    while True:
        r1, r2 = rng.randint(1, TOP), rng.randint(1, TOP)
        if mode == 3:
            r3 = rng.randint(max(r1, r2), min(r1 + r2, TOP))
        else:
            r3 = rng.randint(abs(r1 - r2), min(r1 + r2, TOP))
        top = TOP // 100 if mode == 1 else min(r1, r2)
        if top > 1:
            break
    chain = rng.randint(1, top - 1)
    sys.stdout.write("%d %d %d\n%d\n" % (r1, r2, r3, chain))


if __name__ == "__main__":
    main()
