"""A seed and a mode: mode 1 chooses n uniformly from 0 through 100."""

import random
import sys


def main():
    seed, mode = (int(x) for x in sys.argv[1:])
    if mode != 1:
        raise ValueError("mode must be 1")
    rng = random.Random(seed)
    sys.stdout.buffer.write(f"{rng.randint(0, 100)}\n".encode("ascii"))


main()
