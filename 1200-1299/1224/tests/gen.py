"""Seeded rectangle: SEED BOUND MODE. Mode 1 draws both dimensions
uniformly from 3 through BOUND (at most 2**31 - 1)."""

import random
import sys


def main():
    seed, bound, mode = map(int, sys.argv[1:])
    if mode != 1 or not 3 <= bound <= (1 << 31) - 1:
        raise SystemExit("usage: gen.py SEED BOUND 1; 3 <= BOUND <= 2**31 - 1")
    rng = random.Random(seed)
    rows, columns = rng.randint(3, bound), rng.randint(3, bound)
    sys.stdout.buffer.write(f"{rows} {columns}\n".encode("utf-8"))


if __name__ == "__main__":
    main()
