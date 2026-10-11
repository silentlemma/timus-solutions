"""A seed and a mode: mode 1 chooses N uniformly from 11 through 30;
mode 2 chooses N uniformly from 70 through 98.
"""

import random
import sys


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n = rng.randint(11, 30)
    elif mode == 2:
        n = rng.randint(70, 98)
    else:
        raise ValueError("mode must be 1 or 2")
    sys.stdout.buffer.write(f"{n}\n".encode("ascii"))


main()
