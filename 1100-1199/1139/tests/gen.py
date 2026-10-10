"""Generate a grid: SEED MODE.

Modes:
  multiple: random unequal block sides, one a multiple of the other.
  near-square: random large even block sides differing by two, with exactly
    one interior lattice corner on the diagonal.
"""

import random
import sys

MAX_SIDE = 31998


def main():
    seed, mode = int(sys.argv[1]), sys.argv[2]
    rng = random.Random(seed)
    if mode == "multiple":
        a = rng.randint(3, 300)
        b = a * rng.randint(2, MAX_SIDE // a)
    elif mode == "near-square":
        a = 2 * rng.randint(10000, (MAX_SIDE - 2) // 2)
        b = a + 2
    else:
        raise SystemExit("unknown mode: " + mode)
    if rng.randrange(2):
        a, b = b, a
    sys.stdout.buffer.write(f"{a + 1} {b + 1}\n".encode("ascii"))


if __name__ == "__main__":
    main()
