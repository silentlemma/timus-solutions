"""Generate one deterministic input with python gen.py MODE SEED.

Modes: small and singleton use short random inputs. All other modes have the
maximum length: ones, ones_gap, binary, binary_exact, large, alternating,
exact, gap, feasible, greedy, spikes, all_max, and near_limit.
The importable generate function returns (values, lower, upper).
"""

import random
import sys

MAX_COUNT = 50_000
MAX_FACTOR = 10**9
MAX_PRODUCT = 10**18
SMALL_COUNT = 24
SMALL_BOUND = 1_000
SMALL_FACTORS = (1, 2, 3, 5, 7, 11)
MIN_BINARY_EXPONENT = 20
MAX_BINARY_EXPONENT = 59
EXACT_BINARY_EXPONENTS = (10, 20, 25, 50)
EXACT_DECIMAL_EXPONENTS = (1, 2, 4, 5, 8, 10, 16)
GREEDY_PATTERN = (2, 3, 2, 2)
GREEDY_LOWER = 3
GREEDY_UPPER = 12
FEASIBLE_BLOCKS = ((2, 3), (2, 5), (3, 5), (2, 2, 3))
FEASIBLE_LOWER = 6
FEASIBLE_UPPER = 30
MIN_SPIKE_GAP = 3
MAX_SPIKE_GAP = 101
ARGUMENT_COUNT = 3
MODES = (
    "small",
    "singleton",
    "ones",
    "ones_gap",
    "binary",
    "binary_exact",
    "large",
    "alternating",
    "exact",
    "gap",
    "feasible",
    "greedy",
    "spikes",
    "all_max",
    "near_limit",
)


def generate(mode, seed):
    """Return a valid instance; the minimum count is always a unique integer."""
    rng = random.Random(seed)
    if mode == "small":
        size = rng.randint(1, SMALL_COUNT)
        values = [rng.choice(SMALL_FACTORS) for _ in range(size)]
        if rng.randrange(2):
            lower = rng.randint(1, SMALL_BOUND)
            upper = rng.randint(lower, SMALL_BOUND)
        else:
            start = rng.randrange(size)
            end = rng.randrange(start, size)
            product = 1
            for value in values[start : end + 1]:
                if product > MAX_PRODUCT // value:
                    break
                product *= value
            lower = product if rng.randrange(2) else rng.randint(1, product)
            upper = rng.randint(product, min(MAX_PRODUCT, product * 2))
        return values, lower, upper
    if mode == "singleton":
        value = rng.randint(1, MAX_FACTOR)
        lower = rng.randint(1, value)
        upper = rng.randint(value, MAX_PRODUCT)
        if rng.randrange(2):
            lower = value + 1
            upper = rng.randint(lower, MAX_PRODUCT)
        return [value], lower, upper
    if mode == "ones":
        return [1] * MAX_COUNT, 1, MAX_PRODUCT
    if mode == "ones_gap":
        return [1] * MAX_COUNT, 2, MAX_PRODUCT
    if mode == "binary":
        values = [rng.randint(1, 2) for _ in range(MAX_COUNT)]
        return values, 2**MIN_BINARY_EXPONENT, 2**MAX_BINARY_EXPONENT
    if mode == "binary_exact":
        exponent = rng.choice(EXACT_BINARY_EXPONENTS)
        bound = 2**exponent
        return [2] * MAX_COUNT, bound, bound
    if mode == "large":
        values = [rng.randint(MAX_FACTOR // 2, MAX_FACTOR) for _ in range(MAX_COUNT)]
        return values, 1, MAX_PRODUCT
    if mode == "alternating":
        return [MAX_FACTOR, 1] * (MAX_COUNT // 2), MAX_FACTOR, MAX_FACTOR
    if mode == "exact":
        exponent = rng.choice(EXACT_DECIMAL_EXPONENTS)
        bound = 10**exponent
        return [10] * MAX_COUNT, bound, bound
    if mode == "gap":
        exponent = rng.randint(1, MAX_BINARY_EXPONENT - 1)
        lower = 2**exponent + 1
        upper = 2 ** (exponent + 1) - 1
        values = [rng.randint(1, 2) for _ in range(MAX_COUNT)]
        return values, lower, upper
    if mode == "feasible":
        values = []
        while len(values) < MAX_COUNT:
            block = rng.choice(FEASIBLE_BLOCKS)
            if len(values) + len(block) > MAX_COUNT:
                values.extend([1] * (MAX_COUNT - len(values)))
            else:
                values.extend(block)
        return values, FEASIBLE_LOWER, FEASIBLE_UPPER
    if mode == "greedy":
        values = list(GREEDY_PATTERN) * (MAX_COUNT // len(GREEDY_PATTERN))
        return values, GREEDY_LOWER, GREEDY_UPPER
    if mode == "spikes":
        values = [1] * MAX_COUNT
        position = rng.randrange(MAX_SPIKE_GAP)
        while position < MAX_COUNT:
            values[position] = MAX_FACTOR
            position += rng.randint(MIN_SPIKE_GAP, MAX_SPIKE_GAP)
        return values, MAX_FACTOR, MAX_PRODUCT
    if mode == "all_max":
        return [MAX_FACTOR] * MAX_COUNT, MAX_FACTOR, MAX_PRODUCT
    if mode == "near_limit":
        values = [MAX_FACTOR - 1, MAX_FACTOR] * (MAX_COUNT // 2)
        return values, (MAX_FACTOR - 1) ** 2, MAX_PRODUCT
    raise ValueError("unknown mode: " + mode)


def main():
    if len(sys.argv) != ARGUMENT_COUNT:
        raise SystemExit("usage: python gen.py MODE SEED; modes: " + ", ".join(MODES))
    try:
        values, lower, upper = generate(sys.argv[1], int(sys.argv[2]))
    except ValueError as error:
        raise SystemExit(str(error)) from error
    assert 1 <= len(values) <= MAX_COUNT
    assert 1 <= lower <= upper <= MAX_PRODUCT
    assert all(1 <= value <= MAX_FACTOR for value in values)
    print(len(values), lower, upper)
    print(*values)


if __name__ == "__main__":
    main()
