"""A random network: a seed, N and the shape (random, path, star, deep,
broom). The protocol gives the parent of every computer after the first."""

import random
import sys


def main():
    seed, n, shape = int(sys.argv[1]), int(sys.argv[2]), sys.argv[3]
    rng = random.Random(seed)
    parents = []
    for i in range(2, n + 1):
        if shape == "path":
            p = i - 1
        elif shape == "star":
            p = 1
        elif shape == "deep":
            p = rng.randint(max(1, i - 3), i - 1)
        elif shape == "broom":
            p = i - 1 if i <= n // 2 else rng.randint(1, n // 2)
        else:
            p = rng.randint(1, i - 1)
        parents.append(p)
    sys.stdout.write("\n".join(map(str, [n] + parents)) + "\n")


if __name__ == "__main__":
    main()
