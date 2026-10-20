import random
import sys


MAX_TYPES = 100
MAX_VALUE = 100
MAX_QUERIES = 50_000
MAX_DAYS = 100_000_000
SMALL_TYPES = 6
SMALL_VALUE = 12
SMALL_QUERIES = 40
SMALL_DAYS = 50
TINY_VALUE = 4
TINY_DAYS = 16
DUPLICATE_TYPES = 15
QUERY_BLOCK = 1_000
THRESHOLD_DAYS = 400


def mixed_queries(rng, count):
    boundary = [1, 2, MAX_VALUE, MAX_VALUE + 1, MAX_DAYS - 1, MAX_DAYS]
    queries = boundary[:count]
    while len(queries) < count:
        if len(queries) % 2:
            queries.append(rng.randint(1, THRESHOLD_DAYS))
        else:
            queries.append(rng.randint(1, MAX_DAYS))
    rng.shuffle(queries)
    return queries


def make_case(mode, rng):
    if mode == "small":
        count = rng.randint(1, SMALL_TYPES)
        types = [(rng.randint(1, SMALL_VALUE), rng.randint(1, SMALL_VALUE)) for _ in range(count)]
        queries = [rng.randint(1, SMALL_DAYS) for _ in range(SMALL_QUERIES)]
    elif mode == "tiny":
        types = [(rng.randint(1, TINY_VALUE), rng.randint(1, TINY_VALUE))]
        queries = list(range(1, TINY_DAYS + 1))
        rng.shuffle(queries)
    elif mode == "max-random":
        types = [(rng.randint(1, MAX_VALUE), rng.randint(1, MAX_VALUE)) for _ in range(MAX_TYPES)]
        queries = mixed_queries(rng, MAX_QUERIES)
    elif mode == "max-frontier":
        types = [(value, value) for value in range(1, MAX_VALUE + 1)]
        rng.shuffle(types)
        queries = mixed_queries(rng, MAX_QUERIES)
    elif mode == "max-cheap":
        types = [(1, MAX_VALUE)] * MAX_TYPES
        queries = [MAX_DAYS] * MAX_QUERIES
        queries[0] = 1
        queries[1] = 2
        queries[-1] = MAX_DAYS - 1
    elif mode == "max-expensive":
        types = [(MAX_VALUE, 1)] * MAX_TYPES
        queries = mixed_queries(rng, MAX_QUERIES)
    elif mode == "duplicates":
        base = [
            (rng.randint(1, MAX_VALUE), rng.randint(1, MAX_VALUE)) for _ in range(DUPLICATE_TYPES)
        ]
        types = [rng.choice(base) for _ in range(MAX_TYPES)]
        queries = mixed_queries(rng, QUERY_BLOCK)
    elif mode == "equal-yield":
        types = [(value, MAX_VALUE) for value in range(1, MAX_VALUE + 1)]
        rng.shuffle(types)
        queries = mixed_queries(rng, QUERY_BLOCK)
    elif mode == "equal-cost":
        types = [(MAX_VALUE, value) for value in range(1, MAX_VALUE + 1)]
        rng.shuffle(types)
        queries = mixed_queries(rng, QUERY_BLOCK)
    elif mode == "delayed":
        types = [(MAX_VALUE - value + 1, value) for value in range(1, SMALL_VALUE + 1)]
        rng.shuffle(types)
        queries = list(range(1, THRESHOLD_DAYS + 1))
        rng.shuffle(queries)
    elif mode == "slow-frontier":
        types = [(MAX_VALUE - SMALL_VALUE + value, value) for value in range(1, SMALL_VALUE + 1)]
        rng.shuffle(types)
        queries = mixed_queries(rng, QUERY_BLOCK)
    elif mode == "random-frontier":
        count = rng.randint(1, MAX_TYPES)
        costs = sorted(rng.sample(range(1, MAX_VALUE + 1), count))
        incomes = sorted(rng.sample(range(1, MAX_VALUE + 1), count))
        types = list(zip(costs, incomes))
        rng.shuffle(types)
        queries = mixed_queries(rng, QUERY_BLOCK)
    elif mode == "staircase":
        types = [(value, (value + 1) // 2) for value in range(1, MAX_VALUE + 1)]
        rng.shuffle(types)
        queries = mixed_queries(rng, QUERY_BLOCK)
    elif mode == "thresholds":
        types = [(rng.randint(1, MAX_VALUE), rng.randint(1, MAX_VALUE)) for _ in range(MAX_TYPES)]
        queries = list(range(1, THRESHOLD_DAYS + 1))
        queries.extend([MAX_DAYS, MAX_DAYS - 1, MAX_DAYS // 2])
        rng.shuffle(queries)
    else:
        raise SystemExit("unknown mode")
    return types, queries


def main():
    if len(sys.argv) != 1 + 2:
        raise SystemExit("usage: python gen.py MODE SEED")
    types, queries = make_case(sys.argv[1], random.Random(int(sys.argv[2])))
    lines = [str(len(types))]
    lines.extend(f"{cost} {income}" for cost, income in types)
    lines.append(str(len(queries)))
    lines.extend(map(str, queries))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
