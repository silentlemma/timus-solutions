import random
import sys


MAX_EXPONENT = 18
MAX_QUERIES = 100000
MAX_TEMPERATURE = 100000
SMALL_EXPONENT = 6
SMALL_QUERIES = 100
MEDIUM_EXPONENT = 12
MEDIUM_QUERIES = 10000
LARGE_EXPONENT_CHOICES = 4
SHORT_EXPONENT = 3
ARGUMENT_COUNT = 3

SMALL_RANDOM = 1
SMALL_EXHAUSTIVE = 2
MEDIUM_RANDOM = 3
MAXIMUM_RANDOM = 4
LARGE_INTERVALS = 5
CONSTANT = 6
ALTERNATING = 7
HALVES = 8
RAMP = 9
FULL_RANGE = 10
MEDIUM_EXHAUSTIVE = 11
SINGLETONS = 12
SHORT_INTERVALS = 13


def all_queries(exponent):
    size = 1 << exponent
    return [
        (left, power) for power in range(exponent + 1) for left in range(1, size - (1 << power) + 2)
    ]


def random_queries(rng, exponent, count):
    size = 1 << exponent
    queries = [(1, exponent), (1, 0), (size, 0)]
    while len(queries) < count:
        power = rng.randint(0, exponent)
        left = rng.randint(1, size - (1 << power) + 1)
        queries.append((left, power))
    return queries[:count]


def make_case(mode, rng):
    exponent = MAX_EXPONENT
    count = MAX_QUERIES
    if mode in (SMALL_RANDOM, SMALL_EXHAUSTIVE):
        exponent = rng.randint(1, SMALL_EXPONENT)
        count = rng.randint(1, SMALL_QUERIES)
    elif mode in (MEDIUM_RANDOM, MEDIUM_EXHAUSTIVE):
        exponent = MEDIUM_EXPONENT
        count = MEDIUM_QUERIES

    size = 1 << exponent
    temperatures = [rng.randint(0, MAX_TEMPERATURE) for _ in range(size)]
    if mode == CONSTANT:
        temperatures = [rng.randint(0, MAX_TEMPERATURE)] * size
    elif mode == ALTERNATING:
        temperatures = [MAX_TEMPERATURE * (index % 2) for index in range(size)]
    elif mode == HALVES:
        temperatures = [0] * (size // 2) + [MAX_TEMPERATURE] * (size // 2)
    elif mode == RAMP:
        temperatures = [index * MAX_TEMPERATURE // (size - 1) for index in range(size)]
    elif mode == MEDIUM_EXHAUSTIVE:
        block_size = rng.randint(1, size // 2)
        temperatures = [MAX_TEMPERATURE * ((index // block_size) % 2) for index in range(size)]

    if mode in (SMALL_EXHAUSTIVE, MEDIUM_EXHAUSTIVE):
        queries = all_queries(exponent)
        rng.shuffle(queries)
    elif mode == LARGE_INTERVALS:
        queries = []
        for _ in range(count):
            power = exponent - rng.randrange(LARGE_EXPONENT_CHOICES)
            queries.append((rng.randint(1, size - (1 << power) + 1), power))
    elif mode == FULL_RANGE:
        queries = [(1, exponent)] * count
    elif mode == SINGLETONS:
        queries = [(rng.randint(1, size), 0) for _ in range(count)]
    elif mode == SHORT_INTERVALS:
        queries = []
        for _ in range(count):
            power = rng.randint(0, SHORT_EXPONENT)
            queries.append((rng.randint(1, size - (1 << power) + 1), power))
    else:
        queries = random_queries(rng, exponent, count)
    return exponent, temperatures, queries


def main():
    if len(sys.argv) != ARGUMENT_COUNT:
        raise SystemExit("usage: python gen.py MODE SEED")
    mode = int(sys.argv[1])
    if not SMALL_RANDOM <= mode <= SHORT_INTERVALS:
        raise SystemExit("unknown mode")
    rng = random.Random(int(sys.argv[2]))
    exponent, temperatures, queries = make_case(mode, rng)
    lines = [f"{exponent} {len(queries)}", " ".join(map(str, temperatures))]
    lines.extend(f"{left} {power}" for left, power in queries)
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
