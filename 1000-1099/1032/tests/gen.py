"""Random numbers; a seed, N and the largest number."""

import random
import sys


def main():
    seed, n, top = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    print("\n".join([str(n)] + [str(rng.randint(1, top)) for _ in range(n)]))


if __name__ == "__main__":
    main()
