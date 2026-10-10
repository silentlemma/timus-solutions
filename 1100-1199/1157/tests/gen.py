"""Rectangle counts: a seed and a mode.

Mode 0 chooses two random tile counts in 1..10000 and derives M, N and K
from their rectangle counts, guaranteeing at least one answer in range.
"""

from math import isqrt
import random
import sys


def rectangles(tiles):
    return sum(tiles % width == 0 for width in range(1, isqrt(tiles) + 1))


def main():
    seed, mode = map(int, sys.argv[1:])
    if mode != 0:
        raise ValueError("unknown mode")
    rng = random.Random(seed)
    before = rng.randint(1, 9999)
    after = rng.randint(before + 1, 10000)
    text = f"{rectangles(before)} {rectangles(after)} {after - before}\n"
    sys.stdout.buffer.write(text.encode("ascii"))


if __name__ == "__main__":
    main()
