"""Usage: seed mode. Modes: serial_south_left, serial_north_left,
all_left, no_left, alternating, unequal, synchronous_trap, random.
Each queue has 1000 cars, except the unequal mode with one car from north.
"""

import random
import sys

COUNT = 1000


def generate(seed, mode):
    rng = random.Random(seed)
    if mode == "serial_south_left":
        south, north = "L" * COUNT, "F" * COUNT
    elif mode == "serial_north_left":
        south, north = "R" * COUNT, "L" * COUNT
    elif mode == "all_left":
        south = north = "L" * COUNT
    elif mode == "no_left":
        south, north = ["".join(rng.choices("FR", k=COUNT)) for _ in range(2)]
    elif mode == "alternating":
        south, north = "LF" * (COUNT // 2), "RL" * (COUNT // 2)
    elif mode == "unequal":
        south, north = "".join(rng.choices("FLR", k=COUNT)), "L"
    elif mode == "synchronous_trap":
        south, north = "LF" * (COUNT // 2), "LLF" * (COUNT // 3) + "L"
    elif mode == "random":
        south, north = ["".join(rng.choices("FLR", k=COUNT)) for _ in range(2)]
    else:
        raise ValueError("unknown mode")
    return south + "\n" + north + "\n"


if __name__ == "__main__":
    print(generate(int(sys.argv[1]), sys.argv[2]), end="")
