"""A bed, a goat and a rope: a seed and a mode. Mode 1 gives random
points and rope, mode 2 a rope long enough for the whole bed, mode 3 the
goat on the line through the bed beyond one end."""

import math
import random
import sys

TOP = 10000


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    ax, ay, bx, by = (rng.randint(-TOP, TOP) for _ in range(4))
    cx, cy = rng.randint(-TOP, TOP), rng.randint(-TOP, TOP)
    if mode == 3:
        k = rng.randint(2, 4)  # beyond A by a k-th of the bed
        ax, ay = (rng.randint(-TOP // 2, TOP // 2) for _ in range(2))
        step = TOP // (2 * k)
        dx, dy = (rng.randint(-step, step) for _ in range(2))
        if dx == 0 and dy == 0:
            dx = 1
        bx, by = ax + k * dx, ay + k * dy
        cx, cy = ax - dx, ay - dy
    minimum = 0
    if mode == 2:
        minimum = math.ceil(max(math.hypot(ax - cx, ay - cy), math.hypot(bx - cx, by - cy)))
    rope = rng.randint(minimum, 3 * TOP if mode == 2 else TOP)
    print(ax, ay, bx, by)
    print(cx, cy, rope)


main()
