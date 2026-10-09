"""A random family tree: an acyclic graph on N members with random numbers,
given as lists of children; a seed, N and the percentage of possible
parent-child pairs that are present."""

import random
import sys

PERCENT = 100


def main():
    seed, n, density = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    # members in a hidden order: an edge always goes from earlier to later
    order = rng.sample(range(1, n + 1), n)
    children = {v: [] for v in range(1, n + 1)}
    for i in range(n):
        for j in range(i + 1, n):
            if rng.randrange(PERCENT) < density:
                children[order[i]].append(order[j])
    lines = [str(n)]
    for v in range(1, n + 1):
        rng.shuffle(children[v])
        lines.append(" ".join(map(str, children[v] + [0])))
    print("\n".join(lines))


if __name__ == "__main__":
    main()
