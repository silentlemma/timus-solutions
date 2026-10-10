"""A permutation of 1..N: a seed, N and a mode. Mode 0 shuffles, mode 1
keeps the identity, mode 2 reverses it, mode 3 swaps one random adjacent
pair of the identity."""

import random
import sys


def main():
    seed, n, mode = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    perm = list(range(1, n + 1))
    if mode == 0:
        rng.shuffle(perm)
    elif mode == 2:
        perm.reverse()
    elif mode == 3 and n > 1:
        i = rng.randrange(n - 1)
        perm[i], perm[i + 1] = perm[i + 1], perm[i]
    sys.stdout.write("%d\n%s\n" % (n, " ".join(map(str, perm))))


if __name__ == "__main__":
    main()
