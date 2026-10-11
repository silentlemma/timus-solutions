"""Generate one floor count from a seed and a mode.

Mode 1: a random small building with 1001 to 30000 floors.
Mode 2: a 999-digit building beginning with 12 and a random suffix.
"""

import random
import sys


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    sys.stdout.reconfigure(newline="\n")
    if mode == 1:
        print(rng.randint(1001, 30000))
    elif mode == 2:
        print("12" + "".join(str(rng.randrange(10)) for _ in range(997)))
    else:
        raise ValueError("unknown mode")


main()
