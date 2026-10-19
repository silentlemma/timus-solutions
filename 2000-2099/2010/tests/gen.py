"""Usage: seed mode; modes: corner, opposite_corner, edge_near, edge_middle,
near_corner, even_center, odd_center, random. All use a maximum-size board;
odd_center uses the largest odd side. Randomness is deterministic.
"""

import random
import sys

MAX_SIDE = 100_000_000


def generate(seed, mode):
    rng = random.Random(seed)
    n = MAX_SIDE
    positions = {
        "corner": (1, 1),
        "opposite_corner": (n, n),
        "edge_near": (1, n - 1),
        "edge_middle": (n, n // 2),
        "near_corner": (n - 1, 2),
        "even_center": (n // 2, n // 2 + 1),
        "random": (rng.randint(1, n), rng.randint(1, n)),
    }
    if mode == "odd_center":
        n -= 1
        x = y = (n + 1) // 2
    else:
        x, y = positions[mode]
    return f"{n}\n{x} {y}\n"


if __name__ == "__main__":
    print(generate(int(sys.argv[1]), sys.argv[2]), end="")
