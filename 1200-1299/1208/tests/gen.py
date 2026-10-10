"""Teams: a seed, K and the number of different programmers to draw
from; a small pool makes many teams share members."""

import random
import string
import sys

LONGEST = 20


def main():
    seed, k, pool = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    names = set()
    while len(names) < pool:
        size = rng.randint(1, LONGEST)
        names.add("".join(rng.choice(string.ascii_lowercase) for _ in range(size)))
    names = sorted(names)
    lines = [str(k)] + [" ".join(rng.sample(names, 3)) for _ in range(k)]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
