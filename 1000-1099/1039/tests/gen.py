"""A random hierarchy: a seed, N, the shape (random, chain, star, binary)
and the range of the ratings LOW HIGH. Employees are renumbered at random
and the pairs are listed in random order."""

import random
import sys


def main():
    seed, n = int(sys.argv[1]), int(sys.argv[2])
    shape = sys.argv[3]
    low, high = int(sys.argv[4]), int(sys.argv[5])
    rng = random.Random(seed)
    parent = [0] * n
    for v in range(1, n):
        if shape == "chain":
            parent[v] = v - 1
        elif shape == "star":
            parent[v] = 0
        elif shape == "binary":
            parent[v] = (v - 1) // 2
        else:
            parent[v] = rng.randrange(max(0, v - 50), v)
    label = list(range(1, n + 1))
    rng.shuffle(label)
    lines = [str(n)] + [str(rng.randint(low, high)) for _ in range(n)]
    pairs = ["%d %d" % (label[v], label[parent[v]]) for v in range(1, n)]
    rng.shuffle(pairs)
    sys.stdout.write("\n".join(lines + pairs + ["0 0"]) + "\n")


if __name__ == "__main__":
    main()
