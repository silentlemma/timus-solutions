"""Generate inputs whose queries have at most one unordered valid pair."""

import math
import random
import sys

MAX_SIZE = 100_000
MAX_QUERIES = 100_000
MAX_VALUE = 1_000_000
SMALL_SIZE = 35
MIN_SMALL_QUERIES = 40
MAX_SMALL_QUERIES = 100
SHORT_INTERVAL = 6
QUERY_TRIES = 24
PRIME_RUN = 50_000
LONG_CYCLE = 4
ARGUMENT_COUNT = 3
DENSE_VALUES = (510_510, 570_570, 690_690, 870_870, 930_930)
SAMPLE_VALUES = (4, 6, 8, 9, 25, 49, 121, 10_403, 16_789, 999_983, MAX_VALUE)


def primes():
    sieve = bytearray(b"\x01") * (MAX_VALUE + 1)
    sieve[:2] = b"\x00\x00"
    for prime in range(2, math.isqrt(MAX_VALUE) + 1):
        if sieve[prime]:
            start = prime * prime
            sieve[start::prime] = b"\x00" * ((MAX_VALUE - start) // prime + 1)
    return [value for value in range(2, MAX_VALUE + 1) if sieve[value]]


def unique(values, left, right):
    found = 0
    for first in range(left, right):
        for second in range(first + 1, right + 1):
            if math.gcd(values[first], values[second]) != 1:
                found += 1
                if found > 1:
                    return False
    return True


def random_value(rng):
    if rng.randrange(2):
        return rng.choice(SAMPLE_VALUES)
    return rng.randint(2, MAX_VALUE)


def small(rng):
    size = rng.randint(2, SMALL_SIZE)
    count = rng.randint(MIN_SMALL_QUERIES, MAX_SMALL_QUERIES)
    initial = [random_value(rng) for _ in range(size)]
    values = initial[:]
    operations = []
    for step in range(count):
        if step + 1 != count and rng.randrange(2):
            position = rng.randrange(size)
            value = random_value(rng)
            values[position] = value
            operations.append((2, position + 1, value))
            continue
        for _ in range(QUERY_TRIES):
            left = rng.randrange(size - 1)
            right = rng.randint(left + 1, min(size - 1, left + SHORT_INTERVAL - 1))
            if unique(values, left, right):
                break
        else:
            left = rng.randrange(size - 1)
            right = left + 1
        operations.append((1, left + 1, right + 1))
    return initial, operations


def long(rng):
    run = primes()[:PRIME_RUN]
    values = run * 2
    operations = []
    while len(operations) < MAX_QUERIES:
        offset = rng.randrange(2) * PRIME_RUN
        first, second = sorted(rng.sample(range(PRIME_RUN), 2))
        operations.extend(
            (
                (1, offset + 1, offset + PRIME_RUN),
                (2, offset + second + 1, run[first]),
                (1, offset + 1, offset + PRIME_RUN),
                (2, offset + second + 1, run[second]),
            )
        )
    return values, operations


def dense(rng):
    values = [DENSE_VALUES[0]] * MAX_SIZE
    operations = []
    for step in range(MAX_QUERIES):
        if step % 2 == 0:
            position = rng.randint(1, MAX_SIZE)
            operations.append((2, position, rng.choice(DENSE_VALUES)))
        else:
            left = rng.randrange(1, MAX_SIZE)
            operations.append((1, left, left + 1))
    return values, operations


def sparse(rng):
    choices = primes()[-PRIME_RUN:]
    values = choices * 2
    operations = []
    for step in range(MAX_QUERIES):
        if step % LONG_CYCLE != LONG_CYCLE - 1:
            position = rng.randint(1, MAX_SIZE)
            operations.append((2, position, rng.choice(choices)))
        else:
            left = rng.randrange(1, MAX_SIZE)
            operations.append((1, left, left + 1))
    return values, operations


def generate(mode, seed):
    modes = {"small": small, "long": long, "dense": dense, "sparse": sparse}
    if mode not in modes:
        raise ValueError("mode must be small, long, dense, or sparse")
    values, operations = modes[mode](random.Random(seed))
    lines = ["%d %d" % (len(values), len(operations))]
    lines.append(" ".join(map(str, values)))
    lines.extend("%d %d %d" % operation for operation in operations)
    return "\n".join(lines) + "\n"


def main():
    if len(sys.argv) != ARGUMENT_COUNT:
        raise SystemExit("usage: python gen.py MODE SEED")
    sys.stdout.write(generate(sys.argv[1], int(sys.argv[2])))


if __name__ == "__main__":
    main()
