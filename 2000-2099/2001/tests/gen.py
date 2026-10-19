"""Usage: gen.py SEED MODE; first,second,balanced,baskets,random."""

import random
import sys

LIMIT = 10000


def generate(seed, mode):
    if mode == "first":
        return 0, 0, LIMIT, 0
    if mode == "second":
        return 0, 0, 0, LIMIT
    if mode == "balanced":
        return 0, 0, LIMIT // 2, LIMIT // 2
    if mode == "baskets":
        return LIMIT, LIMIT, 0, 0
    rng = random.Random(seed)
    c, d = rng.randint(0, LIMIT), rng.randint(0, LIMIT)
    total = rng.randint(0, min(LIMIT - c, LIMIT - d))
    x = rng.randint(0, total)
    return c, d, x, total - x


if __name__ == "__main__":
    c, d, x, y = generate(int(sys.argv[1]), sys.argv[2])
    print(c + x, d + y)
    print(c + x + y, d)
    print(c, d + x + y)
