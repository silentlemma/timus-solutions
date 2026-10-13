"""Seeded batches of twenty queries: gen.py MODE SEED.

small: alternate random reachable and unrestricted pairs with endpoints <= 2000.
scaled: random quotients in [2, 10^6] scaled by random legal starting taverns.
"""

import argparse
import random
import sys

MAX_VALUE = 10**9
MAX_QUERIES = 20


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["small", "scaled"])
    parser.add_argument("seed", type=int)
    args = parser.parse_args()
    rng = random.Random(args.seed)
    pairs = []
    for i in range(MAX_QUERIES):
        if args.mode == "small":
            if i % 2 == 0:
                a = rng.randint(1, 40)
                b = a * rng.randint(1, 50)
            else:
                a = rng.randint(1, 2000)
                b = rng.randint(1, 2000)
        else:
            quotient = rng.randint(2, 10**6)
            a = rng.randint(1, MAX_VALUE // quotient)
            b = a * quotient
        pairs.append((a, b))
    text = f"{len(pairs)}\n" + "".join(f"{a} {b}\n" for a, b in pairs)
    sys.stdout.buffer.write(text.encode("utf-8"))


if __name__ == "__main__":
    main()
