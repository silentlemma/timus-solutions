"""Usage: gen.py SEED MODE; dense_short,dense_long,gap,random_short,random_gap,alternating,boundary,short_boundary,long_boundary,hall."""

import random
import sys

VISITORS = 500
MAXIMUM_TIME = 1000000000


def generate(seed, mode):
    rng = random.Random(seed)
    entries = [(i + 1, 0) for i in range(VISITORS)]
    exits = [(VISITORS + i + 1, 1) for i in range(VISITORS)]
    if mode == "dense_short":
        return MAXIMUM_TIME, MAXIMUM_TIME - 2, entries + exits
    if mode == "dense_long":
        return 3, 1, entries + [(MAXIMUM_TIME - VISITORS + i + 1, 1) for i in range(VISITORS)]
    if mode == "gap":
        return MAXIMUM_TIME, 1, entries + exits
    if mode == "short_boundary":
        return MAXIMUM_TIME, VISITORS, entries + exits
    if mode == "long_boundary":
        return VISITORS, 1, entries + exits
    if mode == "alternating":
        return 3, 1, [(i + 1, i % 2) for i in range(2 * VISITORS)]
    if mode == "boundary":
        return VISITORS + 2, VISITORS, entries + exits
    if mode == "hall":
        gadget = [(1, 0), (2, 0), (3, 1), (4, 0), (5, 1), (6, 1)]
        first_unused = len(gadget) + 1
        tail = [(i + first_unused, i % 2) for i in range(2 * VISITORS - len(gadget))]
        return MAXIMUM_TIME, 2, gadget + tail
    directions = [0] * VISITORS + [1] * VISITORS
    rng.shuffle(directions)
    balance = 0
    for i in range(len(directions)):
        if balance == 0 and directions[i] == 1:
            j = next(j for j in range(i + 1, len(directions)) if directions[j] == 0)
            directions[i], directions[j] = directions[j], directions[i]
        balance += 1 if directions[i] == 0 else -1
    limits = {"random_short": (501, 250), "random_gap": (500, 1)}
    a, b = limits[mode]
    return a, b, [(i + 1, d) for i, d in enumerate(directions)]


if __name__ == "__main__":
    minimum_long, maximum_short, events = generate(int(sys.argv[1]), sys.argv[2])
    print(minimum_long, maximum_short)
    print(len(events))
    for time, direction in events:
        print(time, direction)
