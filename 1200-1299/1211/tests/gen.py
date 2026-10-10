"""Deterministic accusation tests. Modes:

SEED T N: legacy random trees, rings, two/no confessors, chains, self-rings.
chain N: one forward chain ending at child N's confession.
tail-cycle N: a long forward tail into a two-cycle, with child N confessing.
stars N: 16 stars with boundary roots, a final self-ring, two/no confessors.
comb SEED T N: random relabelled combs of sizes 20..N, alternating trees
and long spine cycles disconnected from the sole confessor (N >= 20).
"""

import random
import sys


def tree(rng, n):
    order = list(range(1, n + 1))
    rng.shuffle(order)
    names = [0] * n
    for i in range(1, n):
        names[order[i] - 1] = order[rng.randrange(i)]
    return names, order


def structured():
    mode = sys.argv[1]
    if mode == "comb":
        seed, t, limit = map(int, sys.argv[2:])
        assert 1 <= t <= 16 and 20 <= limit <= 25000
        rng = random.Random(seed)
        cases = []
        for case in range(t):
            n = rng.randint(20, limit)
            order = list(range(1, n + 1))
            rng.shuffle(order)
            spine = n // 2
            names = [0] * n
            for i in range(1, spine):
                names[order[i] - 1] = order[i - 1]
            for leaf in order[spine:]:
                names[leaf - 1] = order[rng.randrange(spine)]
            if case % 2:
                names[order[1] - 1] = order[spine - 1]
            cases.append(names)
    else:
        n = int(sys.argv[2])
        assert 3 <= n <= 25000
        if mode == "chain":
            cases = [list(range(2, n + 1)) + [0]]
        elif mode == "tail-cycle":
            cases = [list(range(2, n)) + [n - 2, 0]]
        elif mode == "stars":
            cases = []
            for case in range(16):
                root = 1 if case % 2 == 0 else n
                if case >= 8:
                    root = n // 2 + case % 2
                names = [root] * n
                names[root - 1] = 0
                leaf = n if root != n else n - 1
                kind = (case // 2) % 4
                if kind == 1:
                    names[leaf - 1] = leaf
                elif kind == 2:
                    names[leaf - 1] = 0
                elif kind == 3:
                    names[root - 1] = leaf
                cases.append(names)
        else:
            raise ValueError("unknown mode")
    out = [str(len(cases))]
    for names in cases:
        out.extend([str(len(names)), " ".join(map(str, names))])
    sys.stdout.write("\n".join(out) + "\n")


def main():
    if sys.argv[1] in {"chain", "tail-cycle", "stars", "comb"}:
        structured()
        return
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
