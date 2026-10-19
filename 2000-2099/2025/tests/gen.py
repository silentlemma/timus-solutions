"""Usage: seed mode. Every mode produces 10 test pairs.
Modes: all_singletons, two_equal_groups, two_odd_groups, almost_singletons,
divisors, large_remainders, mixed_extremes, random.
"""

import random
import sys

MAXIMUM = 10000
TESTS = 10


def generate(seed, mode):
    rng = random.Random(seed)
    if mode == "all_singletons":
        pairs = [(MAXIMUM, MAXIMUM)] * TESTS
    elif mode == "two_equal_groups":
        pairs = [(MAXIMUM, 2)] * TESTS
    elif mode == "two_odd_groups":
        pairs = [(MAXIMUM - 1, 2)] * TESTS
    elif mode == "almost_singletons":
        pairs = [(MAXIMUM, MAXIMUM - 1)] * TESTS
    elif mode == "divisors":
        divisors = [k for k in range(2, MAXIMUM + 1) if MAXIMUM % k == 0]
        pairs = [(MAXIMUM, k) for k in divisors[:TESTS]]
    elif mode == "large_remainders":
        pairs = [(MAXIMUM, k) for k in (3, 7, 13, 99, 101, 333, 999, 3333, 5000, 5001)]
    elif mode == "mixed_extremes":
        pairs = [(2, 2), (MAXIMUM, MAXIMUM)] * (TESTS // 2)
    elif mode == "random":
        pairs = [(MAXIMUM, rng.randint(2, MAXIMUM)) for _ in range(TESTS)]
    else:
        raise ValueError("unknown mode")
    assert len(pairs) == TESTS
    return str(TESTS) + "\n" + "".join(f"{n} {k}\n" for n, k in pairs)


if __name__ == "__main__":
    print(generate(int(sys.argv[1]), sys.argv[2]), end="")
