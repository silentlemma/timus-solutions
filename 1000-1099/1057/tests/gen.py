"""A random query: a seed, the largest width of the range (0 for any) and
K and B (0 for random)."""

import random
import sys

LIMIT = 2**31 - 1


def main():
    seed, width, k, b = (int(v) for v in sys.argv[1:5])
    rng = random.Random(seed)
    b = b or rng.randint(2, 10)
    k = k or rng.randint(1, 20)
    if width:
        x = rng.randint(1, LIMIT - width)
        y = x + rng.randint(0, width)
    else:
        x, y = sorted(rng.randint(1, LIMIT) for _ in range(2))
    sys.stdout.write("%d %d\n%d\n%d\n" % (x, y, k, b))


if __name__ == "__main__":
    main()
