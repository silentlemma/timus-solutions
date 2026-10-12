"""A bed, a goat and a rope: a seed and a mode. Mode 1 gives random
points and rope, mode 2 a rope long enough for the whole bed, mode 3 the
goat on the line through the bed beyond one end."""

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
        cx = max(-TOP, min(TOP, ax + (ax - bx) // k))
        cy = max(-TOP, min(TOP, ay + (ay - by) // k))
    rope = rng.randint(0, 3 * TOP if mode == 2 else TOP)
    print(ax, ay, bx, by)
    print(cx, cy, rope)


main()
