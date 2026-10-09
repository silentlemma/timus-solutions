"""Random queries: a seed and how many (at most ten)."""

import random
import sys

TOP = 99999


def main():
    seed, count = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    lines = [str(rng.randint(1, TOP)) for _ in range(count)] + ["0"]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
