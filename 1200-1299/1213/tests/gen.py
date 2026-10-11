"""A cargo module: a seed, the number of compartments and the number of
extra partitions on top of a random tree; names differ in letter case
now and then."""

import random
import string
import sys

LONGEST = 20
SYMBOLS = string.ascii_letters + string.digits


def main():
    seed, n, extra = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    names = []
    while len(names) < n:
        if names and rng.random() < 0.2:
            name = rng.choice(names).swapcase()
        else:
            name = "".join(rng.choice(SYMBOLS) for _ in range(rng.randint(1, LONGEST)))
        if name not in names:
            names.append(name)
    edges = {(names[i], names[rng.randrange(i)]) for i in range(1, n)}
    for _ in range(extra):
        a, b = rng.sample(names, 2) if n > 1 else (names[0], names[0])
        if (a, b) not in edges and (b, a) not in edges and a != b:
            edges.add((a, b))
    edges = list(edges)
    rng.shuffle(edges)
    lines = [rng.choice(names)] + ["%s-%s" % e for e in edges] + ["#"]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
