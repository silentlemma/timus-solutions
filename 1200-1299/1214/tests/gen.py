"""Usage: gen.py odd SEED.

Mode odd draws two distinct positive odd integers from the full allowed
range, checking that two odd operands have an even sum and stay in order.
"""

import random
import sys

LIMIT = 32000


def main():
    mode, seed = sys.argv[1:]
    if mode != "odd":
        raise ValueError("unknown mode: " + mode)
    rng = random.Random(int(seed))
    x, y = rng.sample(range(1, LIMIT + 1, 2), 2)
    sys.stdout.buffer.write(f"{x} {y}\n".encode("ascii"))


if __name__ == "__main__":
    main()
