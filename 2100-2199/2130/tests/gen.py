"""Generate a deterministic input: python gen.py MODE SEED."""

import math
import random
import sys

MAX_COUNT = 100000
MAX_DIVISOR = 1000000
SMALL_COUNT = 100
ARGUMENT_COUNT = 3
PRIME_THREE = 3
PRIME_FIVE = 5
PRIME_SEVEN = 7
COMPOSITE_SIX = 6
POWER_TWO = 19
POWER_THREE = 12
LARGE_PRIMES = (999983, 999979)
HIDDEN_VALUES = (1, 524288, 390625, 73513440, 999962000357, 999999000000)
SPECIAL_DIVISORS = (1, 2, 3, 5, 6, 7, 12, 49, 64, 999983, 999999, MAX_DIVISOR)


def divisors(value):
    result = []
    for divisor in range(1, min(math.isqrt(value), MAX_DIVISOR) + 1):
        if value % divisor == 0:
            result.append(divisor)
            other = value // divisor
            if other != divisor and other <= MAX_DIVISOR:
                result.append(other)
    return sorted(result)


def random_rows(rng, count):
    rows = []
    for _ in range(count):
        if rng.randrange(2):
            divisor = rng.choice(SPECIAL_DIVISORS)
        else:
            divisor = rng.randint(1, MAX_DIVISOR)
        rows.append((divisor, rng.randrange(2)))
    return rows


def feasible_rows(rng, count):
    hidden = rng.choice(HIDDEN_VALUES)
    positive = divisors(hidden)
    rows = []
    for _ in range(count):
        if rng.randrange(2):
            rows.append((rng.choice(positive), 1))
        else:
            divisor = rng.randint(2, MAX_DIVISOR)
            while hidden % divisor == 0:
                divisor = rng.randint(2, MAX_DIVISOR)
            rows.append((divisor, 0))
    return rows


def power_rows(rng):
    growth = []
    for base, exponent in ((2, POWER_TWO), (PRIME_THREE, POWER_THREE)):
        value = 1
        for _ in range(exponent):
            value *= base
            growth.append((value, 1))
    growth.append((PRIME_FIVE, 1))
    negative = {MAX_DIVISOR}
    target = MAX_COUNT - len(growth)
    while len(negative) < target:
        prime = rng.choice((PRIME_FIVE, PRIME_SEVEN))
        negative.add(prime * rng.randint(1, MAX_DIVISOR // prime))
    rows = [(value, 0) for value in sorted(negative)]
    rng.shuffle(rows)
    return rows + growth


def generate(mode, seed):
    rng = random.Random(seed)
    if mode == "small":
        return random_rows(rng, rng.randint(1, SMALL_COUNT))
    if mode == "feasible":
        return feasible_rows(rng, rng.randint(1, SMALL_COUNT))
    if mode == "mixed":
        return feasible_rows(rng, MAX_COUNT)
    if mode == "negative":
        rows = [(MAX_DIVISOR, 0)]
        rows += [(rng.randint(2, MAX_DIVISOR), 0) for _ in range(MAX_COUNT - 1)]
        return rows
    if mode == "positive":
        positive = divisors(HIDDEN_VALUES[-1])
        return [(rng.choice(positive), 1) for _ in range(MAX_COUNT)]
    if mode == "late":
        tail = [(2, 1), (PRIME_THREE, 1)]
        rows = [(COMPOSITE_SIX, 0)]
        rows += [
            (rng.randint(PRIME_SEVEN, MAX_DIVISOR), 0) for _ in range(MAX_COUNT - len(tail) - 1)
        ]
        return rows + tail
    if mode == "overflow":
        first, second = LARGE_PRIMES
        if rng.randrange(2):
            first, second = second, first
        rows = [(rng.choice((1, first)), 1) for _ in range(MAX_COUNT - 2)]
        rows[0] = (first, 1)
        return rows + [(second, 1), (2, 1)]
    if mode == "powers":
        return power_rows(rng)
    if mode == "unique":
        return [(1, 0)] + random_rows(rng, MAX_COUNT - 1)
    raise SystemExit("unknown mode: " + mode)


def main():
    if len(sys.argv) != ARGUMENT_COUNT:
        raise SystemExit("usage: python gen.py MODE SEED")
    rows = generate(sys.argv[1], int(sys.argv[2]))
    assert 1 <= len(rows) <= MAX_COUNT
    assert all(1 <= divisor <= MAX_DIVISOR and positive in (0, 1) for divisor, positive in rows)
    lines = [str(len(rows))]
    lines += ["%d %d" % row for row in rows]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
