"""Generate a connected elevator system from MODE and SEED.

Modes: small, random, chain, dense, nested, bottleneck, single, staircase.
Every mode except small uses the maximum number of elevators. Random, chain,
nested, bottleneck and staircase also use the maximum number of floors.
"""

import argparse
import random
import sys

LIMIT = 10**5
SMALL = 10
MODES = (
    "small",
    "random",
    "chain",
    "dense",
    "nested",
    "bottleneck",
    "single",
    "staircase",
)


def generate(mode, rng):
    if mode == "small":
        floors = rng.randint(1, SMALL)
        count = rng.randint(1, SMALL)
        links = rng.randint(1, min(count, max(1, floors - 1)))
        stops = [1] + sorted(rng.sample(range(2, floors), links - 1)) + [floors]
        intervals = list(zip(stops, stops[1:]))
        for _ in range(count - links):
            left = rng.randint(1, floors)
            intervals.append((left, rng.randint(left, floors)))
    elif mode == "dense":
        floors = 2
        intervals = [(1, floors)] * LIMIT
    elif mode == "single":
        floors = 1
        intervals = [(1, 1)] * LIMIT
    else:
        floors = LIMIT
        if mode == "chain":
            intervals = [(floor, floor + 1) for floor in range(1, floors)]
            intervals.append((floors, floors))
        elif mode == "staircase":
            intervals = [(floor, floor + 2) for floor in range(1, floors - 1)]
            intervals.extend([(1, 2), (floors - 1, floors)])
        elif mode == "nested":
            intervals = [
                (offset + 1, floors - offset)
                for offset in (index % (floors // 2) for index in range(LIMIT))
            ]
        elif mode == "bottleneck":
            cut = rng.randint(1, floors - 1)
            intervals = [(1, floors)]
            for _ in range(LIMIT - 1):
                low, high = rng.choice(((1, cut), (cut + 1, floors)))
                left = rng.randint(low, high)
                intervals.append((left, rng.randint(left, high)))
        else:
            intervals = [(1, floors)]
            for _ in range(LIMIT - 1):
                left = rng.randint(1, floors)
                intervals.append((left, rng.randint(left, floors)))
    rng.shuffle(intervals)
    return floors, intervals


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=MODES)
    parser.add_argument("seed", type=int)
    args = parser.parse_args()
    floors, intervals = generate(args.mode, random.Random(args.seed))
    lines = [f"{floors} {len(intervals)}"]
    lines.extend(f"{left} {right}" for left, right in intervals)
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
