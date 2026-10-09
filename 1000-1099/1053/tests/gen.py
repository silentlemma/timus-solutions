"""Random lengths: a seed, N and the common factor (0 for random lengths).
With a factor f, every length is f times a random number, so the answer is
a multiple of f."""

import random
import sys

LIMIT = 2**31 - 1


def main():
    seed, n, factor = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    if factor:
        lengths = [factor * rng.randint(1, LIMIT // factor) for _ in range(n)]
    else:
        lengths = [rng.randint(1, LIMIT) for _ in range(n)]
    sys.stdout.write("\n".join([str(n)] + list(map(str, lengths))) + "\n")


if __name__ == "__main__":
    main()
