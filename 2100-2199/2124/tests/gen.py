import random
import sys


MAX_SIZE = 100_000
SMALL_SIZE = 32
SMALL_QUERIES = 100
MANY_FACTOR_PRIME = 106_696_591
MAX_FACTOR_PRIME = 892_371_481
LARGE_PRIME = 999_999_937
POWER_PRIME = 998_244_353
SUBGROUP_ORDER = 119
SUBGROUP_INDEX = 23
PRIMES = (
    2,
    3,
    5,
    7,
    17,
    31,
    97,
    257,
    1009,
    65_537,
    MANY_FACTOR_PRIME,
    MAX_FACTOR_PRIME,
    POWER_PRIME,
    LARGE_PRIME,
)
MODES = (
    "small",
    "mixed",
    "updates",
    "singletons",
    "subgroups",
    "full",
    "queries",
    "prime2",
    "factors",
    "proper",
)


def prime_factors(value):
    factors = []
    divisor = 2
    while divisor * divisor <= value:
        if value % divisor == 0:
            factors.append(divisor)
            while value % divisor == 0:
                value //= divisor
        divisor += 1
    if value > 1:
        factors.append(value)
    return factors


def primitive_root(prime):
    order = prime - 1
    factors = prime_factors(order)
    candidate = 2
    while any(pow(candidate, order // factor, prime) == 1 for factor in factors):
        candidate += 1
    return candidate


def main():
    if len(sys.argv) != 1 + 2 or sys.argv[1] not in MODES:
        raise SystemExit("usage: python gen.py MODE SEED; modes: " + ", ".join(MODES))
    mode = sys.argv[1]
    rng = random.Random(int(sys.argv[2]))
    size = MAX_SIZE
    query_count = MAX_SIZE
    prime = MANY_FACTOR_PRIME
    if mode == "small":
        prime = rng.choice(PRIMES)
        size = rng.randint(1, SMALL_SIZE)
        query_count = rng.randint(1, SMALL_QUERIES)
    elif mode in ("updates", "subgroups"):
        prime = POWER_PRIME
    elif mode in ("singletons", "full"):
        prime = LARGE_PRIME
    elif mode == "prime2":
        prime = 2
    elif mode in ("factors", "proper"):
        prime = MAX_FACTOR_PRIME

    subgroup = None
    subgroup_base = None
    if mode == "subgroups":
        root = primitive_root(prime)
        generator = pow(root, (prime - 1) // SUBGROUP_ORDER, prime)
        subgroup = [pow(generator, exponent, prime) for exponent in range(SUBGROUP_ORDER)]
        values = [rng.choice(subgroup) for _ in range(size)]
    elif mode == "proper":
        subgroup_base = pow(primitive_root(prime), SUBGROUP_INDEX, prime)
        values = [pow(subgroup_base, rng.randrange(prime - 1), prime) for _ in range(size)]
    else:
        values = [rng.randint(1, prime - 1) for _ in range(size)]

    lines = [f"{prime} {size} {query_count}", " ".join(map(str, values))]
    for _ in range(query_count):
        left = rng.randint(1, size)
        right = rng.randint(left, size)
        if mode == "singletons":
            right = left
        elif mode == "full":
            left, right = 1, size
        if mode == "updates":
            update = True
        elif mode == "queries":
            update = False
        elif mode in ("factors", "proper"):
            update = rng.randrange(10) != 0
            if mode == "factors" and not update:
                right = left
        else:
            update = rng.randrange(2) == 0
        if update:
            if subgroup_base is not None:
                multiplier = pow(subgroup_base, rng.randrange(prime - 1), prime)
            else:
                multiplier = rng.choice(subgroup) if subgroup else rng.randint(1, prime - 1)
            lines.append(f"1 {left} {right} {multiplier}")
        else:
            lines.append(f"2 {left} {right}")
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
