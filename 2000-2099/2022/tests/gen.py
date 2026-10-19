"""Usage: seed mode. Eight integer parameters, all between 1 and 1000.
Modes: all_maximum, large_integer_positive, two_components, ceiling_tangent,
near_landing, apex_before, apex_after, switching_apex, short_domain, random_full,
near_minimum_margin.
The input size is constant; modes exercise numerical and geometric extremes.
"""

import random
import sys

from checker import EPS, intervals

MAX_VALUE = 1000


def generate(seed, mode):
    rng = random.Random(seed)
    fixed = {
        "all_maximum": (1000, 1000, 1000, 1000, 1000, 1000, 1000, 1000),
        "large_integer_positive": (1000, 900, 1, 100, 1000, 1000, 1000, 1000),
        "two_components": (10, 1, 5, 7, 1, 10, 10, 10),
        "ceiling_tangent": (10, 1, 5, 9, 1, 10, 10, 10),
        "near_landing": (999, 4, 1, 1, rng.randint(4, 8), 1, 1000, 10),
        "apex_before": (1000, 1000, 1, 1000, 1, 1000, 100, 1),
        "apex_after": (10, 1, 5, 199, 1, 1, 10, 100),
        "switching_apex": (11, 1, 1, 6, 10, 10, 10, 10),
        "short_domain": (2, 1, 1, 10, 1000, 1000, 1000, 1000),
        "near_minimum_margin": (998, 4, 1, 1, 1, 10, 999, 10),
    }
    if mode == "random_full":
        while True:
            data = tuple(rng.randint(1, MAX_VALUE) for _ in range(8))
            parts = intervals(data)
            # Feasibility must imply a full time window of width greater than 2*EPS.
            if not parts or any(hi - lo > 2 * EPS for lo, hi in parts):
                break
    else:
        data = fixed[mode]
    return " ".join(map(str, data[:4])) + "\n" + " ".join(map(str, data[4:])) + "\n"


if __name__ == "__main__":
    print(generate(int(sys.argv[1]), sys.argv[2]), end="")
