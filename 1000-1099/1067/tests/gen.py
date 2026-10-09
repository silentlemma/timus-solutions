"""Random folder lists: a seed, N, the number of distinct folder names, the
shortest and the longest name, and the most folders in one path. Names come
from all allowed characters, so special characters sort around the letters."""

import random
import sys

ALLOWED = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!#$%&'()-@^_`{}~"
LONGEST_PATH = 80


def main():
    seed, n, pool, shortest, longest, depth = (int(x) for x in sys.argv[1:7])
    rng = random.Random(seed)
    names = set()
    while len(names) < pool:
        size = rng.randint(shortest, longest)
        names.add("".join(rng.choice(ALLOWED) for _ in range(size)))
    names = sorted(names)
    paths = []
    seen = set()
    while len(paths) < n:
        parts = []
        for _ in range(rng.randint(1, depth)):
            name = rng.choice(names)
            if len("\\".join(parts + [name])) > LONGEST_PATH:
                break
            parts.append(name)
        path = "\\".join(parts)
        if path not in seen:
            seen.add(path)
            paths.append(path)
    sys.stdout.write("\n".join([str(n)] + paths) + "\n")


if __name__ == "__main__":
    main()
