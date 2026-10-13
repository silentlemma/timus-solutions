"""One test from a seed and a mode: a random triangulation of the polygon
is built by splitting vertex intervals, and part of its diagonals are
given. Mode 1 is 50000 vertices with half the cuts given, mode 2 with
none, mode 3 with all, mode 4 is a fan of cuts from one vertex, mode 5
is a small polygon. Mode 6 is a deeply nested chain, mode 7 an alternating
ear triangulation with one cut missing, and mode 8 sparse random cuts from
a random ear triangulation. Modes 6-8 accept an optional vertex count
(default 50000) as the third argument."""

import random
import sys

LARGEST = 50000
SMALL = 10


def extra_mode(rng, mode, n):
    if mode == 6:
        cuts = [(a, n + 1 - a) for a in range(2, (n - 1) // 2 + 1)]
    elif mode == 7:
        cuts = []
        lo, hi = 1, n
        while hi - lo + 1 > 3:
            if len(cuts) % 2 == 0:
                lo += 1
            else:
                hi -= 1
            cuts.append((lo, hi))
        if cuts:
            cuts.pop(len(cuts) // 2)
    elif mode == 8:
        left = [n - 1] + list(range(n - 1))
        right = list(range(1, n)) + [0]
        active = list(range(n))
        cuts = []
        while len(active) > 3:
            index = rng.randrange(len(active))
            v = active[index]
            a, b = left[v], right[v]
            cuts.append((a + 1, b + 1))
            right[a], left[b] = b, a
            active[index] = active[-1]
            active.pop()
        cuts = rng.sample(cuts, min(len(cuts), max(1, n // 500)))
    else:
        raise ValueError("unknown mode")
    cuts = [edge if rng.randrange(2) else edge[::-1] for edge in cuts]
    rng.shuffle(cuts)
    print(n)
    print(len(cuts))
    for a, b in cuts:
        print(a, b)


def main():
    seed, mode = (int(a) for a in sys.argv[1:3])
    rng = random.Random(seed)
    if mode in (6, 7, 8):
        n = int(sys.argv[3]) if len(sys.argv) > 3 else LARGEST
        if not 3 <= n <= LARGEST:
            raise ValueError("vertex count must be between 3 and 50000")
        extra_mode(rng, mode, n)
        return
    n = rng.randint(3, SMALL) if mode == 5 else LARGEST
    if mode == 4:
        cuts = [(1, v) for v in range(3, n)]
    else:
        cuts = []
        stack = [(1, n)]
        while stack:
            a, b = stack.pop()
            if b - a < 2:
                continue
            c = rng.randint(a + 1, b - 1)
            for lo, hi in ((a, c), (c, b)):
                if hi - lo >= 2:
                    cuts.append((lo, hi))
                    stack.append((lo, hi))
    share = {1: 0.5, 2: 0.0, 3: 1.0, 4: 0.5, 5: rng.random()}[mode]
    given = [c if rng.random() < 0.5 else c[::-1] for c in cuts if rng.random() < share]
    rng.shuffle(given)
    print(n)
    print(len(given))
    for a, b in given:
        print(a, b)


main()
