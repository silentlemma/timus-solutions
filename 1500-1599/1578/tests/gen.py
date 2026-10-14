"""One test: seed mode [total], with N + 2 different points.

Mode 1: 2002 random points. Mode 2: a rounded sloping line (legacy).
Mode 3: a dense grid. Mode 4: a rounded circle. Mode 5: 3 to 6 random points.
Mode 6: an exact diagonal line. Mode 7: two tight opposite corner clusters.
Mode 8: random points on the two extreme horizontal borders.
Modes 6 to 8 accept an optional total point count; defaults are 2002, 2002,
and 2001 respectively. Existing modes ignore this optional argument.
"""

import math
import random
import sys

TURNS = 2000
TOP = 2000
FEW = 6


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    total = rng.randint(3, FEW) if mode == 5 else TURNS + 2
    if mode in (6, 7, 8):
        total = int(sys.argv[3]) if len(sys.argv) > 3 else TURNS + (1 if mode == 8 else 2)
        if not 3 <= total <= TURNS + 2:
            raise ValueError("total must be between 3 and 2002")
    pts = set()
    if mode == 2:
        pts = {(x, 2 * x // 3) for x in rng.sample(range(-TOP, TOP + 1), total)}
    elif mode == 3:
        side = int(math.isqrt(total)) + 1
        grid = [(x, y) for x in range(side) for y in range(side)]
        pts = set(rng.sample(grid, total))
    elif mode == 4:
        while len(pts) < total:
            a = rng.uniform(0, 2 * math.pi)
            pts.add((round(TOP * math.cos(a)), round(TOP * math.sin(a))))
    elif mode == 6:
        pts = {(x, -x) for x in rng.sample(range(-TOP, TOP + 1), total)}
    elif mode == 7:
        low = [(x, y) for x in range(-TOP, -TOP + 32) for y in range(-TOP, -TOP + 32)]
        high = [(x, y) for x in range(TOP - 31, TOP + 1) for y in range(TOP - 31, TOP + 1)]
        pts = set(rng.sample(low, (total + 1) // 2) + rng.sample(high, total // 2))
    elif mode == 8:
        border = [(x, y) for x in range(-TOP, TOP + 1) for y in (-TOP, TOP)]
        pts = set(rng.sample(border, total))
    else:
        while len(pts) < total:
            pts.add((rng.randint(-TOP, TOP), rng.randint(-TOP, TOP)))
    pts = list(pts)
    rng.shuffle(pts)
    print(total - 2)
    for x, y in pts:
        print(x, y)


main()
