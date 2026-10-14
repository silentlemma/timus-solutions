"""One n from a seed and a mode.

Mode 1 picks n in [200, 900]; mode 2 picks an odd n in [1001, 1997];
mode 3 picks an even n in [1400, 1998].
"""

import random
import sys


def main():
    seed, mode = (int(x) for x in sys.argv[1:])
    rng = random.Random(seed)
    low, high, step = {1: (200, 900, 1), 2: (1001, 1997, 2), 3: (1400, 1998, 2)}[mode]
    print(rng.randrange(low, high + 1, step))


if __name__ == "__main__":
    main()
