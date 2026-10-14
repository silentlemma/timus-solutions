"""One length from a seed and a mode. Mode 1 picks n in [101, 4095];
mode 2 picks n in [4096, 9998], below the existing upper-bound cases.
"""

import random
import sys


def main():
    seed, mode = (int(x) for x in sys.argv[1:])
    low, high = {1: (101, 4095), 2: (4096, 9998)}[mode]
    print(random.Random(seed).randint(low, high))


if __name__ == "__main__":
    main()
