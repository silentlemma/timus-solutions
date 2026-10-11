"""K and M: a seed and a mode. Mode 1 draws both anywhere; mode 2 puts M
at or a little above the place K has when N = K, so an answer exists; mode
3 takes a small K and a large M, so N is many digits longer than K."""

import random
import sys

LIMIT = 10**9
SMALL_K = 1000
NEAR = 1000


def place_at_k(k):
    """The position of K among 1..K in lexicographic order."""
    digits = str(k)
    return sum(int(digits[:size]) - 10 ** (size - 1) + 1 for size in range(1, len(digits) + 1))


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        k, m = rng.randint(1, LIMIT), rng.randint(1, LIMIT)
    elif mode == 2:
        k = rng.randint(1, LIMIT)
        m = min(LIMIT, place_at_k(k) + rng.randint(0, NEAR))
    else:
        k, m = rng.randint(1, SMALL_K), rng.randint(LIMIT - NEAR * NEAR, LIMIT)
    sys.stdout.write("%d %d\n" % (k, m))


if __name__ == "__main__":
    main()
