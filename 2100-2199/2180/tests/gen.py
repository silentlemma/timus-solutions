"""Usage: python gen.py MODE SEED.

Small modes: small_random, small_chain, small_star, small_balanced, small_broom.
Maximal modes: chain, star, balanced, broom, random, stress, forks, updates, queries,
int64.
All modes use seeded randomness and print one valid input with a unique answer.
"""

import random
import sys


MAX_VERTICES = 100000
MAX_OPERATIONS = 100000
MAX_VALUE = 1000000000
SMALL_VERTICES = 40
SMALL_OPERATIONS = 80
BRANCH_DIVISOR = 3
BOUNDARY_PERIOD = 5
QUERY_PERIOD = 3


def make_parents(shape, count, rng):
    parents = [0] * (count + 1)
    spine = max(2, count // BRANCH_DIVISOR)
    first_end = 1 + (count - 1) // 2
    for vertex in range(2, count + 1):
        if shape == "chain":
            parent = vertex - 1
        elif shape == "star":
            parent = 1
        elif shape == "balanced":
            parent = vertex // 2
        elif shape == "broom":
            parent = vertex - 1 if vertex <= spine else spine
        elif shape == "stress":
            parent = vertex - 1 if vertex <= spine else rng.randint(1, spine)
        elif shape == "forks":
            parent = 1 if vertex == first_end + 1 else vertex - 1
        else:
            parent = rng.randint(1, vertex - 1)
        parents[vertex] = parent
    return parents


def make_operations(mode, count, operations, rng):
    spine = max(2, count // BRANCH_DIVISOR)
    first_end = 1 + (count - 1) // 2
    for index in range(operations):
        vertex = rng.randint(1, count)
        if mode == "queries":
            yield f"? {vertex}"
            continue
        if mode == "int64":
            if index + 1 == operations:
                yield f"? {count}"
            else:
                yield f"+ 1 {count} {MAX_VALUE}"
            continue
        if mode == "forks":
            if index % 10 == 0:
                yield f"? {vertex}"
            else:
                if rng.randrange(2):
                    lower, upper = 2, first_end
                else:
                    lower, upper = first_end + 1, count
                vertex = rng.randint(lower, upper - 2)
                limit = rng.randint(1, upper - vertex - 1)
                value = rng.randint(1, MAX_VALUE)
                yield f"+ {vertex} {limit} {value}"
            continue
        if mode == "stress":
            if index % 2:
                vertex = rng.randint(spine + 1, count)
                yield f"? {vertex}"
            else:
                vertex = rng.randint(1, spine)
                limit = rng.randint(0, count)
                if index % BOUNDARY_PERIOD:
                    limit = rng.randint(0, spine - vertex + 1)
                value = rng.randint(1, MAX_VALUE)
                yield f"+ {vertex} {limit} {value}"
            continue
        if mode != "updates" and index % QUERY_PERIOD == 0:
            yield f"? {vertex}"
            continue
        boundary = index % BOUNDARY_PERIOD
        if boundary == 0:
            limit = 0
        elif boundary == 1:
            limit = count
        elif boundary == 2:
            limit = 1
        else:
            limit = rng.randint(0, count)
        value = MAX_VALUE if rng.randrange(2) else rng.randint(1, MAX_VALUE)
        yield f"+ {vertex} {limit} {value}"


def main():
    mode, seed = sys.argv[1:]
    small = mode.startswith("small_")
    shape = mode.removeprefix("small_")
    modes = {"chain", "star", "balanced", "broom", "random", "stress", "forks"}
    if shape not in modes and mode not in {"updates", "queries", "int64"}:
        raise SystemExit("unknown mode")
    if small and shape in {"stress", "forks"}:
        raise SystemExit("stress and forks are maximal modes")
    rng = random.Random(int(seed))
    count = rng.randint(2, SMALL_VERTICES) if small else MAX_VERTICES
    operations = rng.randint(1, SMALL_OPERATIONS) if small else MAX_OPERATIONS
    if mode == "int64":
        shape = "chain"
    parents = make_parents(shape, count, rng)
    lines = [str(count), " ".join(map(str, parents[2:])), str(operations)]
    lines.extend(make_operations(mode, count, operations, rng))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
