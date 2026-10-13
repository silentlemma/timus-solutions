"""Seeded batches of twenty numbers: gen.py MODE SEED.

small: random numbers in [2, 10000], for dense small-number coverage.
wide: random numbers throughout [2, 10^9].
window: twenty consecutive numbers starting at a random point in [10^5, 10^8].
"""

import argparse
import random
import sys

MAX_VALUE = 10**9
MAX_COUNT = 20


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["small", "wide", "window"])
    parser.add_argument("seed", type=int)
    args = parser.parse_args()
    rng = random.Random(args.seed)
    if args.mode == "small":
        numbers = [rng.randint(2, 10000) for _ in range(MAX_COUNT)]
    elif args.mode == "wide":
        numbers = [rng.randint(2, MAX_VALUE) for _ in range(MAX_COUNT)]
    else:
        start = rng.randint(10**5, 10**8)
        numbers = list(range(start, start + MAX_COUNT))
    text = f"{len(numbers)}\n" + "".join(f"{n}\n" for n in numbers)
    sys.stdout.buffer.write(text.encode("utf-8"))


if __name__ == "__main__":
    main()
