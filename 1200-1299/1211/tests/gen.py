"""Tests of accusations: a seed, T and N. Each test is one of: a tree
around one confessor, a tree with one ring cut into it, two confessors,
no confessor, a single long chain, or someone accusing themselves."""

import random
import sys


def tree(rng, n):
    order = list(range(1, n + 1))
    rng.shuffle(order)
    names = [0] * n
    for i in range(1, n):
        names[order[i] - 1] = order[rng.randrange(i)]
    return names, order


def main():
    seed, t, n = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    out = [str(t)]
    for case in range(t):
        kind = case % 6
        names, order = tree(rng, n)
        if kind == 1 and n >= 3:
            ring = rng.sample(order[1:], rng.randint(2, n - 1))
            for a, b in zip(ring, ring[1:] + ring[:1]):
                names[a - 1] = b
        elif kind == 2 and n >= 2:
            names[order[rng.randrange(1, n)] - 1] = 0
        elif kind == 3:
            names[order[0] - 1] = rng.randint(1, n)
        elif kind == 4:
            names = [0] * n
            for i in range(1, n):
                names[order[i] - 1] = order[i - 1]
        elif kind == 5 and n >= 2:
            v = order[rng.randrange(1, n)]
            names[v - 1] = v
        out += [str(n), " ".join(map(str, names))]
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
