"""Random distinct stars listed by Y, then X; a seed, N and the largest
coordinate."""

import random
import sys


def main():
    seed, n, top = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    stars = set()
    while len(stars) < n:
        stars.add((rng.randint(0, top), rng.randint(0, top)))
    lines = [str(n)] + ["%d %d" % s for s in sorted(stars, key=lambda s: (s[1], s[0]))]
    print("\n".join(lines))


if __name__ == "__main__":
    main()
