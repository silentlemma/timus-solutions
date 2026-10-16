"""One test from a seed and a mode: mode 1 a random number of fishermen
up to the limit, mode 2 exactly the limit, mode 3 the limit with only
the extreme throws 0 and n - 1."""

import random
import sys

LIMIT = 2000


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(2, LIMIT) if mode == 1 else LIMIT
    if mode == 3:
        thrown = [rng.choice((0, n - 1)) for _ in range(n)]
    else:
        thrown = [rng.randrange(n) for _ in range(n)]
    print(n)
    print(*thrown)


main()
