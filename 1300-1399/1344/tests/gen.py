"""A chain of movable pulleys: a seed and a mode. Each movable pulley
hangs on one end of the rope over the next one, and the last hangs on a
fixed pulley. Mode 1 puts the free rope on the first axle and the turnip
on the fixed pulley, mode 2 the other way round, mode 3 hangs the turnip
on a chain tied to the ceiling and the free rope on a separate pair of
pulleys, mode 4 the longest chain."""

import random
import sys

CEILING, TURNIP, FREE = 0, -1, -2
LONGEST = 31


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    k = LONGEST if mode == 4 else rng.randint(2, 20)
    first, last = (TURNIP, FREE) if mode == 2 else (FREE, TURNIP)
    if mode == 3:
        k = rng.randint(2, 20)
        first = TURNIP
    blocks = []
    for i in range(1, k + 1):
        load = first if i == 1 else i - 1  # the axle hangs on the previous rope
        ends = [CEILING, i + 1] if i < k or mode != 3 else [CEILING, CEILING]
        rng.shuffle(ends)
        blocks.append([2, *ends, load])
    if mode == 3:
        # a fixed pulley and a movable one on the same rope, with the free load
        blocks.append([1, k + 2, k + 2, CEILING])
        blocks.append([2, k + 1, k + 1, FREE])
    else:
        blocks.append([1, k, last, CEILING])
    print(len(blocks))
    for b in blocks:
        print(*b)


main()
