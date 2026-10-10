"""Weights of stripies: a seed, N and the largest weight."""

import random
import sys


def main():
    seed, n, top = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    sys.stdout.write("%d\n%s\n" % (n, "\n".join(str(rng.randint(1, top)) for _ in range(n))))


if __name__ == "__main__":
    main()
