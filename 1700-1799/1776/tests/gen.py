"""One test from a seed and a mode: a random number of rockets, mode 1
from 3 to 20, mode 2 from 3 to 400."""

import random
import sys

FEWEST = 3
FEW = 20
MOST = 400


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    print(rng.randint(FEWEST, FEW if mode == 1 else MOST))


main()
