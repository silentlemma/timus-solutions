"""Moments of the four elements and two armies: a seed, the sizes of the
armies and a mode. Mode 0 is random, mode 1 puts moments at the very
start and end of the day, mode 2 gives both armies the same mages, mode 3
uses round times and powers so that ties are likely."""

import random
import sys

DAY = 24 * 60 * 60
MINUTE = 60
TOP = 10000
HOUR = MINUTE * MINUTE
ROUND = 100


def clock(t):
    return "%02d:%02d:%02d" % (t // HOUR, t // MINUTE % MINUTE, t % MINUTE)


def main():
    seed, light, dark, mode = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    lines = []
    for e in "AEFW":
        if mode == 1:
            strong, weak = rng.sample([0, 1, DAY - 2, DAY - 1, rng.randrange(DAY)], 2)
        elif mode == 3:
            strong, weak = (HOUR * h for h in rng.sample(range(24), 2))
        else:
            strong, weak = rng.sample(range(DAY), 2)
        if mode == 3:
            top, low = rng.randint(1, ROUND) * ROUND, rng.randint(1, ROUND) * ROUND
        else:
            top, low = rng.randint(1, TOP), rng.randint(1, TOP)
        lines.append("%s %s %d %s %d" % (e, clock(strong), top, clock(weak), low))
    army = "".join(rng.choice("AEFW") for _ in range(light))
    lines.append(army)
    lines.append(army if mode == 2 else "".join(rng.choice("AEFW") for _ in range(dark)))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
