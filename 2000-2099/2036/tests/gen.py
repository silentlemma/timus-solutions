"""Generate maximum distinct point sets.

Modes: line_horizontal, line_slanted, near_first, near_middle, near_last,
grid, late_two, grid_permuted. Every mode has 100000 initial points.
"""

import random
import sys

MAX_N = 100000
COORD = 100000000


def generate(seed, mode):
    if mode == "line_horizontal":
        return [(x, COORD) for x in range(-MAX_N // 2, MAX_N // 2)]
    if mode == "line_slanted":
        scale = 1000
        return [(x * scale, -x * scale) for x in range(-MAX_N // 2, MAX_N // 2)]
    if mode.startswith("near_"):
        intercept = 3
        points = [(x, 2 * x + intercept) for x in range(-MAX_N // 2 + 1, MAX_N // 2)]
        at = {"near_first": 0, "near_middle": MAX_N // 2, "near_last": MAX_N - 1}[mode]
        points.insert(at, (COORD, -COORD))
        return points
    if mode == "late_two":
        intercept = 3
        points = [(x, 2 * x + intercept) for x in range(-MAX_N // 2 + 1, MAX_N // 2 - 1)]
        return points + [(COORD, -COORD), (-COORD, -COORD)]
    if mode in ("grid", "grid_permuted"):
        width = 100
        points = [(i // width, i % width) for i in range(MAX_N)]
        if mode == "grid_permuted":
            random.Random(seed).shuffle(points)
        return points
    raise ValueError("Unknown mode")


def main():
    points = generate(int(sys.argv[1]), sys.argv[2])
    print(len(points))
    sys.stdout.write("".join(f"{x} {y}\n" for x, y in points))


if __name__ == "__main__":
    main()
