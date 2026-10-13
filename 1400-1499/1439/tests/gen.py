"""Random battles: a seed, the number of rooms, the number of lines, the
number of destroyed rooms and a mode. Mode 1 picks doors at random, mode 2
always destroys the first room, mode 3 the last one."""

import random
import sys


def main():
    seed, n, m, d, mode = (int(a) for a in sys.argv[1:6])
    rng = random.Random(seed)
    kinds = ["D"] * d + ["L"] * (m - d)
    rng.shuffle(kinds)
    rooms = n
    lines = ["%d %d" % (n, m)]
    for kind in kinds:
        if kind == "D" and mode == 2:
            number = 1
        elif kind == "D" and mode == 3:
            number = rooms
        else:
            number = rng.randint(1, rooms)
        lines.append("%s %d" % (kind, number))
        if kind == "D":
            rooms -= 1
    print("\n".join(lines))


main()
