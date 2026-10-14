"""One test from a seed and a mode: claims made by pairs of students.
Mode 1 is 1000 students with true debts and 100000 claims, mode 2 the
same plus one false claim, mode 3 a bipartite plan (no odd cycle), mode 4
a single odd cycle through everyone, mode 5 is small, and mode 6 is a
random branching tree attached to a triangle, with half-integral debts."""

import random
import sys

STUDENTS = 1000
CLAIMS = 100000
TOP = 5000
SMALL = 6


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 6:
        # One odd cycle fixes the tree, even after labels and claims are shuffled.
        labels = list(range(1, STUDENTS + 1))
        rng.shuffle(labels)
        twice = [2 * rng.randrange(-TOP, TOP) + 1 for _ in labels]
        pairs = [(0, 1), (1, 2), (2, 0)]
        pairs.extend((v, rng.randrange(v)) for v in range(3, STUDENTS))
        rng.shuffle(pairs)
        print(STUDENTS, len(pairs))
        for u, v in pairs:
            print(labels[u], labels[v], (twice[u] + twice[v]) // 2)
        return
    n = rng.randint(2, SMALL) if mode == 5 else STUDENTS
    debt = [rng.randint(-TOP, TOP) for _ in range(n)]
    pairs = set()
    if mode == 4:
        # an odd ring through everyone: the debts are fixed, with halves
        ring = n if n % 2 else n - 1
        pairs = {tuple(sorted((i, (i + 1) % ring))) for i in range(ring)}
        if ring < n:
            pairs.add((0, n - 1))
    else:
        want = min(CLAIMS, n * (n - 1) // 2) if mode != 5 else rng.randint(1, n * (n - 1) // 2)
        # a path through everyone keeps the plan connected
        order = list(range(n))
        rng.shuffle(order)
        pairs = {tuple(sorted((order[i], order[i + 1]))) for i in range(n - 1)}
        while len(pairs) < want:
            a, b = rng.sample(range(n), 2)
            if mode == 3 and a % 2 == b % 2:
                continue
            pairs.add(tuple(sorted((a, b))))
        if mode == 3:
            pairs = {p for p in pairs if p[0] % 2 != p[1] % 2}
    claims = [(a, b, debt[a] + debt[b]) for a, b in pairs]
    rng.shuffle(claims)
    if mode == 2:
        a, b, s = claims[0]
        claims[0] = (a, b, s + 1)
    print(n, len(claims))
    for a, b, s in claims:
        print(a + 1, b + 1, s)


main()
