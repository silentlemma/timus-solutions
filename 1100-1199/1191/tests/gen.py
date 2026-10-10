"""A chase: a seed, N and the largest interval; L and the intervals are
random in 1..99, intervals up to the given largest."""

import random
import sys

LIMIT = 99


def main():
    seed, n, top = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    lines = [
        "%d %d" % (rng.randint(1, LIMIT), n),
        " ".join(str(rng.randint(1, top)) for _ in range(n)),
    ]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
