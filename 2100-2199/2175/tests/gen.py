import random
import sys


MAX_SIZE = 100000
MAX_VALUE = 1000000000
SMALL_SIZE = 60
SMALL_QUERIES = 150
SMALL_VALUE = 30
MEDIUM_SIZE = 2000
MEDIUM_QUERIES = 3000
HIDDEN_SIZE = 600
HIDDEN_QUERIES = 1000
RANDOM = 1
EQUAL = 2
ORDERED = 3
REPLACEMENTS = 4
MEDIUM_RANDOM = 5
HIDDEN = 6
MAX_RANDOM = 7
MAX_ASCENDING = 8
MAX_DESCENDING = 9
MAX_REPLACEMENTS = 10
MAX_SWEEP = 11
MAX_ACCUMULATION = 12
MAX_REVERSE = 13


def generate(mode, rng):
    if mode == RANDOM:
        size = rng.randint(1, SMALL_SIZE)
        values = [rng.randint(0, SMALL_VALUE) for _ in range(size)]
        queries = rng.randint(1, SMALL_QUERIES)
        changes = [(rng.randrange(size), rng.randint(0, SMALL_VALUE)) for _ in range(queries)]
    elif mode == EQUAL:
        size = rng.randint(1, SMALL_SIZE)
        values = [rng.choice((0, 1, MAX_VALUE))] * size
        queries = SMALL_QUERIES
        changes = [(rng.randrange(size), rng.choice((0, 1, 2, MAX_VALUE))) for _ in range(queries)]
    elif mode == ORDERED:
        size = rng.randint(2, SMALL_SIZE)
        values = list(range(size))
        if rng.randrange(2):
            values.reverse()
        changes = [(0, 0), (size - 1, 0), (0, size)]
        changes.extend(
            (rng.randrange(size), rng.choice((0, 1, size))) for _ in range(SMALL_QUERIES)
        )
    elif mode == REPLACEMENTS:
        size = rng.randint(2, SMALL_SIZE)
        values = list(range(size))
        changes = [(0, size)]
        changes.extend((index % 2, rng.choice((0, 1, 2))) for index in range(SMALL_QUERIES))
    elif mode == MEDIUM_RANDOM:
        size = rng.randint(MEDIUM_SIZE // 2, MEDIUM_SIZE)
        values = [rng.randint(0, MAX_VALUE) for _ in range(size)]
        changes = [(rng.randrange(size), rng.randint(0, MAX_VALUE)) for _ in range(MEDIUM_QUERIES)]
    elif mode == HIDDEN:
        size = rng.randint(HIDDEN_SIZE // 2, HIDDEN_SIZE)
        values = [MAX_VALUE] + [rng.randint(0, SMALL_VALUE) for _ in range(size - 1)]
        changes = [
            (rng.randrange(1, size), rng.randint(0, SMALL_VALUE)) for _ in range(HIDDEN_QUERIES)
        ]
        changes.extend(((size - 1, MAX_VALUE), (0, MAX_VALUE)))
    elif mode == MAX_RANDOM:
        size = MAX_SIZE
        values = [rng.randint(0, MAX_VALUE) for _ in range(size)]
        changes = [(rng.randrange(size), rng.randint(0, MAX_VALUE)) for _ in range(MAX_SIZE)]
    elif mode == MAX_ASCENDING:
        size = MAX_SIZE
        values = list(range(size))
        changes = [
            (rng.randrange(size), 0) if index % 2 else (size - 1, 1) for index in range(MAX_SIZE)
        ]
    elif mode == MAX_DESCENDING:
        size = MAX_SIZE
        values = [MAX_VALUE - index for index in range(size)]
        changes = [(rng.randrange(1, size), rng.choice((0, 1, 2))) for _ in range(MAX_SIZE)]
    elif mode == MAX_REPLACEMENTS:
        size = MAX_SIZE
        values = list(range(size))
        changes = [(index % 2, MAX_VALUE) for index in range(MAX_SIZE)]
    elif mode == MAX_SWEEP:
        size = MAX_SIZE
        values = list(range(size))
        changes = [(index, MAX_VALUE) for index in range(MAX_SIZE)]
    elif mode == MAX_ACCUMULATION:
        size = MAX_SIZE
        values = [MAX_VALUE] * size
        changes = [(0, MAX_VALUE)] * MAX_SIZE
    else:
        size = MAX_SIZE
        values = [0] * size
        changes = [(index, 1) for index in range(size - 1, -1, -1)]
    return values, changes


def main():
    mode = int(sys.argv[1])
    seed = int(sys.argv[2])
    if mode < RANDOM or mode > MAX_REVERSE:
        raise ValueError("unknown generator mode")
    values, changes = generate(mode, random.Random(seed))
    lines = [str(len(values)), " ".join(map(str, values)), str(len(changes))]
    lines.extend(f"{position + 1} {delta}" for position, delta in changes)
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
