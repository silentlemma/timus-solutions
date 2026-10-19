"""Usage: seed mode. Fixed maximum families (seed accepted for the interface):
zero_chain, zero_cycle, positive_chain, positive_cycle, late_chain, late_cycle,
different_merge, same_merge, reset_merge, star. All have 100000 vertices;
chains have 99999 edges, other families have 100000. Targets are sorted.
"""

import sys

COUNT = 100000
LABEL_A = 7
LABEL_B = 9
RESET = 42


def generate(_seed, mode):
    values = [0] * COUNT
    graph = [[i + 1] for i in range(COUNT - 1)] + [[]]
    if mode in ("zero_cycle", "positive_cycle", "late_cycle"):
        graph[-1] = [0]
    if mode in ("positive_chain", "positive_cycle"):
        values = list(range(1, COUNT + 1))
    elif mode in ("late_chain", "late_cycle"):
        values[-1] = COUNT
    elif mode in ("different_merge", "same_merge", "reset_merge"):
        graph[0], graph[1], graph[2] = [1, 2], [3], [3]
        values[1], values[2] = LABEL_A, LABEL_A if mode == "same_merge" else LABEL_B
        if mode == "reset_merge":
            values[4] = RESET
    elif mode == "star":
        graph = [list(range(COUNT))] + [[] for _ in range(COUNT - 1)]
        values[0] = COUNT
    elif mode not in ("zero_chain", "zero_cycle"):
        raise ValueError("unknown mode")
    return (
        str(COUNT)
        + "\n"
        + "".join(
            " ".join(map(str, [value, len(row)] + [v + 1 for v in row])) + "\n"
            for value, row in zip(values, graph)
        )
    )


if __name__ == "__main__":
    print(generate(int(sys.argv[1]), sys.argv[2]), end="")
