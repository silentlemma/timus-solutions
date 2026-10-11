"""A class of 10 with a connected call graph: a seed and a mode. Mode 1
gives a random tree, mode 2 a random graph with about half of the pairs,
mode 3 a tree with a few extra pairs, mode 4 every pair. Names are random
words of up to 20 letters."""

import random
import string
import sys

N = 10
LONGEST = 20
DENSITY = {1: 0, 2: 0.5, 3: 0.1, 4: 1}  # share of extra pairs by mode


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    names = set()
    while len(names) < N:
        names.add("".join(rng.choice(string.ascii_letters) for _ in range(rng.randint(1, LONGEST))))
    names = sorted(names)
    rng.shuffle(names)
    pairs = {(i, rng.randrange(i)) for i in range(1, N)}
    extra = DENSITY[mode]
    for a in range(N):
        for b in range(a):
            if rng.random() < extra:
                pairs.add((a, b))
    pairs = [rng.choice([p, p[::-1]]) for p in pairs]
    rng.shuffle(pairs)
    print(N)
    print(len(pairs))
    for a, b in pairs:
        print(names[a], names[b])
    print(names[rng.randrange(N)])


main()
