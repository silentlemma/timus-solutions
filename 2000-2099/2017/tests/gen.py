"""Usage: seed mode. All modes have 400 people.
Modes: balanced_dense (K200,200), skew_dense (K399,1), no_conflicts,
shared_witness (K250,150), pairs, path, one_edge_many_isolates, random.
Random testimonies come from two internally consistent location assignments.
"""

import random
import sys

COUNT = 400
HALF = COUNT // 2
SHARED_LEFT = 250
PLACE_LENGTH = 20


def generate(seed, mode):
    rng = random.Random(seed)
    n = COUNT
    locations = ["a"] * HALF + ["b"] * HALF
    seen = [[j for j in range(n) if i != j] for i in range(n)]
    if mode == "skew_dense":
        locations = ["a"] * (n - 1) + ["b"]
    elif mode == "no_conflicts":
        locations = ["a" * PLACE_LENGTH] * n
    elif mode == "shared_witness":
        locations = ["a"] * SHARED_LEFT + ["b"] * (n - SHARED_LEFT)
        seen = [[]] + [[0] for _ in range(n - 1)]
    elif mode in ("pairs", "path"):
        locations = ["a" if i % 2 == 0 else "b" for i in range(n)]
        seen = (
            [[i ^ 1] for i in range(n)]
            if mode == "pairs"
            else ([[i + 1] for i in range(n - 1)] + [[]])
        )
    elif mode == "one_edge_many_isolates":
        locations = ["a", "b"] + ["a"] * (n - 2)
        seen = [[], [0]] + [[] for _ in range(n - 2)]
    elif mode == "random":
        sides = [rng.randrange(2) for _ in range(n)]
        places = ["a" * PLACE_LENGTH, "b" * PLACE_LENGTH, "c" * PLACE_LENGTH]
        assignments = [[rng.choice(places) for _ in range(n)] for _ in range(2)]
        locations = [assignments[sides[i]][i] for i in range(n)]
        seen = [
            [
                j
                for j in range(n)
                if j != i and assignments[sides[i]][j] == locations[i] and rng.randrange(2)
            ]
            for i in range(n)
        ]
    elif mode != "balanced_dense":
        raise ValueError("unknown mode")
    lines = [str(n)]
    for location, row in zip(locations, seen):
        lines.append(" ".join(map(str, [location, len(row)] + [v + 1 for v in row])))
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    print(generate(int(sys.argv[1]), sys.argv[2]), end="")
