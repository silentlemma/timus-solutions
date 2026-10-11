"""Cargo module modes:

SEED N EXTRA: original random tree plus attempted extra partitions;
names differ in letter case now and then.
small SEED N EXTRA: 1 <= N <= 12 rooms, a random tree and exactly EXTRA
additional partitions, with deterministic partition ordering.
"""

import random
import string
import sys

LONGEST = 20
SYMBOLS = string.ascii_letters + string.digits


def small():
    seed, n, extra = (int(x) for x in sys.argv[2:])
    if not 1 <= n <= 12 or not 0 <= extra <= (n - 1) * (n - 2) // 2:
        raise ValueError("invalid room or extra partition count")
    rng = random.Random(seed)
    names = []
    while len(names) < n:
        name = "".join(rng.choice(SYMBOLS) for _ in range(rng.randint(1, LONGEST)))
        if name not in names:
            names.append(name)
    edges = {(rng.randrange(i), i) for i in range(1, n)}
    unused = [(a, b) for a in range(n) for b in range(a + 1, n) if (a, b) not in edges]
    rng.shuffle(unused)
    ordered = sorted(edges) + unused[:extra]
    rng.shuffle(ordered)
    lines = [rng.choice(names)]
    for a, b in ordered:
        if rng.randrange(2):
            a, b = b, a
        lines.append(f"{names[a]}-{names[b]}")
    sys.stdout.write("\n".join(lines + ["#"]) + "\n")


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
    if sys.argv[1] == "small":
        small()
    else:
        main()
