"""N, A and B: a seed. Each from 1 to 100."""

import random
import sys

TOP = 100


def main():
    rng = random.Random(int(sys.argv[1]))
    print(*(rng.randint(1, TOP) for _ in range(3)))


if __name__ == "__main__":
    main()
