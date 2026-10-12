"""Mersenne-prime queries: SEED MODE COUNT.

random: COUNT independent uniform queries with indices 1 through 17.
balanced: COUNT copies of every index 1 through 17, shuffled together.
runs: COUNT queries in random constant runs of at most 10000 queries.

Restrict indices to 17 so generated answers can also be checked by exhaustive
Lucas-Lehmer enumeration in a small independent oracle.
"""

import argparse
import random
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("seed", type=int)
    parser.add_argument("mode", choices=("random", "balanced", "runs"))
    parser.add_argument("count", type=int)
    args = parser.parse_args()
    if args.count < 1:
        parser.error("count must be positive")
    rng = random.Random(args.seed)
    if args.mode == "random":
        queries = [rng.randint(1, 17) for _ in range(args.count)]
    elif args.mode == "balanced":
        queries = list(range(1, 18)) * args.count
        rng.shuffle(queries)
    else:
        queries = []
        previous = 0
        while len(queries) < args.count:
            value = rng.choice([n for n in range(1, 18) if n != previous])
            queries.extend([value] * min(10000, args.count - len(queries)))
            previous = value
    sys.stdout.reconfigure(newline="\n")
    print(len(queries))
    print("\n".join(map(str, queries)))


if __name__ == "__main__":
    main()
