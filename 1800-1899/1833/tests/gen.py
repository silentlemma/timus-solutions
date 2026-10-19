"""One school from a seed and a mode: mode 1 a few canoeists with
random crews, mode 2 the most canoeists and crews at random, mode 3 a
long odd cycle with chords, mode 4 a complete bipartite graph, mode 5
sparse random crews where many canoeists sit in no crew."""

import random
import sys

LIMIT = 500
CREWS = 100000
TOP = 10000
SMALL = 9


def main():
    seed, mode = (int(v) for v in sys.argv[1:3])
    rng = random.Random(seed)
    n = rng.randint(2, SMALL) if mode == 1 else LIMIT
    k = rng.randint(1, TOP)
    crews = set()
    if mode == 3:
        for v in range(n - 1 if n % 2 == 0 else n):
            crews.add((v, (v + 1) % (n - 1 if n % 2 == 0 else n)))
        for _ in range(n):
            a, b = rng.sample(range(n), 2)
            crews.add((a, b))
    elif mode == 4:
        half = rng.randint(1, n - 1)
        crews = {(a, b) for a in range(half) for b in range(half, n)}
        crews = set(rng.sample(sorted(crews), min(CREWS, len(crews))))
    else:
        most = n * (n - 1) // 2
        count = rng.randint(0, most) if mode == 1 else (CREWS if mode == 2 else n // 3)
        while len(crews) < min(count, most):
            a, b = rng.sample(range(n), 2)
            if (b, a) not in crews:
                crews.add((a, b))
    crews = list(crews)
    rng.shuffle(crews)
    labels = list(range(1, n + 1))
    rng.shuffle(labels)
    print(n, k, len(crews))
    for a, b in crews:
        print(labels[a], labels[b])


main()
