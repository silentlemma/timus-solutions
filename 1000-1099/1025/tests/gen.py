"""Random odd group sizes; a seed, the odd number of groups K and the largest
group size. The population stays within LIMIT."""

import random
import sys

LIMIT = 9999


def main():
    seed, k, top = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    sizes = []
    for i in range(k):
        room = LIMIT - sum(sizes) - (k - i - 1)
        sizes.append(rng.randrange(1, min(top, room) + 1, 2))
    print(k)
    print(" ".join(map(str, sizes)))


if __name__ == "__main__":
    main()
