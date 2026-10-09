"""A random query: a seed, the largest N and the largest K. K is drawn up
to one past the number of strings of length N, so most queries have an
answer."""

import random
import sys


def main():
    seed, top_n, top_k = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    n = rng.randint(1, top_n)
    a, b = 1, 2
    for _ in range(n - 1):
        a, b = b, a + b
    sys.stdout.write("%d %d\n" % (n, rng.randint(1, min(top_k, b + 1))))


if __name__ == "__main__":
    main()
