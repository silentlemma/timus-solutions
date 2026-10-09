"""A random query: a seed and the largest index; L is random from 1 to 14."""

import random
import sys


def main():
    seed, top = int(sys.argv[1]), int(sys.argv[2])
    rng = random.Random(seed)
    sys.stdout.write("%d %d\n" % (rng.randint(0, top), rng.randint(1, 14)))


if __name__ == "__main__":
    main()
