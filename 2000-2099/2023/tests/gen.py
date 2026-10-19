"""Usage: seed mode. All modes produce 1000 names.
Modes: all_left, all_middle, all_right, alternating_extremes,
cabinet_cycle, all_names, longest_name, random.
"""

import random
import sys

COUNT = 1000
GROUPS = (
    ("Alice", "Ariel", "Aurora", "Phil", "Peter", "Olaf", "Phoebus", "Ralph", "Robin"),
    ("Bambi", "Belle", "Bolt", "Mulan", "Mowgli", "Mickey", "Silver", "Simba", "Stitch"),
    ("Dumbo", "Genie", "Jiminy", "Kuzko", "Kida", "Kenai", "Tarzan", "Tiana", "Winnie"),
)


def generate(seed, mode):
    rng = random.Random(seed)
    names = sum(GROUPS, ())
    if mode in ("all_left", "all_middle", "all_right"):
        group = ("all_left", "all_middle", "all_right").index(mode)
        result = rng.choices(GROUPS[group], k=COUNT)
    elif mode == "alternating_extremes":
        result = ["Dumbo" if index % 2 == 0 else "Alice" for index in range(COUNT)]
    elif mode == "cabinet_cycle":
        result = [GROUPS[index % len(GROUPS)][0] for index in range(COUNT)]
    elif mode == "all_names":
        result = [names[index % len(names)] for index in range(COUNT)]
    elif mode == "longest_name":
        result = ["Phoebus"] * COUNT
    elif mode == "random":
        result = rng.choices(names, k=COUNT)
    else:
        raise ValueError("unknown mode")
    return str(COUNT) + "\n" + "\n".join(result) + "\n"


if __name__ == "__main__":
    print(generate(int(sys.argv[1]), sys.argv[2]), end="")
