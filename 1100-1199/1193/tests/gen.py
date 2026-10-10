"""An exam: a seed, N and a mode. Preparation times are distinct, from 0
to 600; answers last 1 to 240 minutes. Mode 0 gives deadlines anywhere
from the end of preparation to 600, mode 1 tight deadlines just after
preparation, mode 2 all students ready at nearly the same time."""

import random
import sys

LATEST = 600
LONGEST = 240


def main():
    seed, n, mode = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    ready = rng.sample(range(0, 40) if mode == 2 else range(LATEST + 1), n)
    lines = [str(n)]
    for t1 in ready:
        t2 = rng.randint(1, LONGEST)
        t3 = min(LATEST, t1 + rng.randint(0, 10)) if mode == 1 else rng.randint(t1, LATEST)
        lines.append("%d %d %d" % (t1, t2, t3))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
