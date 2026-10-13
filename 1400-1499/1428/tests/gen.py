"""Seeded exponent triples: SEED MODE.

Mode 1: unequal non-unit divisors of C-1, with C composite.
Mode 2: unequal non-unit divisors of C-1, with C prime.
Each mode chooses uniformly from its valid ordered triples.
"""

import random
import sys


def main():
    sys.stdout.reconfigure(newline="\n")
    seed, mode = map(int, sys.argv[1:])
    if mode not in (1, 2):
        raise SystemExit("mode must be 1 or 2")
    triples = []
    for c in range(4, 33):
        prime = all(c % d for d in range(2, c))
        if prime != (mode == 2):
            continue
        divisors = [d for d in range(2, c) if (c - 1) % d == 0]
        triples.extend((a, b, c) for a in divisors for b in divisors if a != b)
    print(*random.Random(seed).choice(triples))


if __name__ == "__main__":
    main()
