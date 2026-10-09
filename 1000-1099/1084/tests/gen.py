"""A random garden: a seed and the largest side and rope."""

import random
import sys


def main():
    seed, top = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    side = rng.randint(1, top)
    # most ropes reach past the middle of a side but not the corners
    rope = rng.randint(side // 2, max(side // 2, round(side * 0.7)))
    if rng.random() < 0.2:
        rope = rng.randint(1, top)
    sys.stdout.write("%d %d\n" % (side, max(1, rope)))


if __name__ == "__main__":
    main()
