"""A random pair of flights: a seed, then optionally the shift in hours.
Durations are up to six hours and differ by at most ten minutes."""

import random
import sys

DAY = 24 * 60
LONGEST = 6 * 60
SPREAD = 10
MAX_SHIFT = 5


def clock(t):
    t %= DAY
    return "%02d.%02d" % (t // 60, t % 60)


def main():
    rng = random.Random(int(sys.argv[1]))
    if len(sys.argv) > 2:
        shift = int(sys.argv[2])
    else:
        shift = rng.randint(-MAX_SHIFT, MAX_SHIFT)
    there = rng.randint(SPREAD, LONGEST)
    back = rng.randint(there - SPREAD, min(LONGEST, there + SPREAD))
    out1 = rng.randrange(DAY)
    out2 = rng.randrange(DAY)
    # the second airport is shift hours ahead of the first one
    lines = [
        clock(out1) + " " + clock(out1 + there + shift * 60),
        clock(out2) + " " + clock(out2 + back - shift * 60),
    ]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
