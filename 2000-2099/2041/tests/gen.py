"""Generate seed mode with 100000 items.

Modes: all_wide, unique_points, equal_points, tight_supply, short_supply,
endpoint_equality, shared_bridges, random_mixed, deletion_queries,
minimum_points, maximum_points. Every mode shuffles input IDs independently.
"""

import random
import sys

SIZE = 100000
VOLUME = 1000000
HALF = SIZE // 2
QUARTER = SIZE // 4
CENTER = VOLUME // 2


def build(seed, mode):
    rng = random.Random(seed)
    if mode == "all_wide":
        dolls = [(1, VOLUME)] * SIZE
    elif mode == "unique_points":
        dolls = [(i + 1, i + 1) for i in range(SIZE)]
    elif mode == "equal_points":
        dolls = [(CENTER, CENTER)] * SIZE
    elif mode == "tight_supply":
        dolls = [(CENTER, CENTER)] * HALF + [(1, VOLUME)] * (HALF - 1) + [(1, 2)]
    elif mode == "short_supply":
        dolls = [(CENTER, CENTER)] * HALF + [(1, VOLUME)] * (HALF - 2) + [(1, 2)] * 2
    elif mode == "endpoint_equality":
        dolls = [(CENTER, CENTER)] * HALF + [(CENTER, VOLUME)] * HALF
    elif mode == "shared_bridges":
        low, high = VOLUME * 3 // 10, VOLUME * 7 // 10
        dolls = [(low, low)] * QUARTER + [(high, high)] * QUARTER
        dolls += [(1, VOLUME)] * (QUARTER - 1) + [(1, 2)] * (QUARTER + 1)
    elif mode == "random_mixed":
        dolls = []
        for _ in range(SIZE):
            a = rng.randrange(1, VOLUME + 1)
            b = a if rng.random() < 0.5 else rng.randrange(a, VOLUME + 1)
            dolls.append((a, b))
    elif mode == "deletion_queries":
        dolls = [(i + 1, VOLUME - i) for i in range(SIZE)]
    elif mode == "minimum_points":
        dolls = [(1, 1)] * HALF + [(1, VOLUME)] * HALF
    elif mode == "maximum_points":
        dolls = [(VOLUME, VOLUME)] * HALF + [(1, VOLUME)] * HALF
    else:
        raise ValueError("Unknown mode")
    rng.shuffle(dolls)
    return dolls


def main():
    dolls = build(int(sys.argv[1]), sys.argv[2])
    print(len(dolls))
    sys.stdout.write("".join(f"{a} {b}\n" for a, b in dolls))


if __name__ == "__main__":
    main()
