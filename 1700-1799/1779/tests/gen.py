"""One test from a seed and a mode: a random number of students, mode 1
from 3 to 20, mode 2 from 3 to 200."""

import random
import sys

FEWEST = 3
FEW = 20
MOST = 200


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    print(rng.randint(FEWEST, FEW if mode == 1 else MOST))


main()
