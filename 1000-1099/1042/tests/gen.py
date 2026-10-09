"""A random invertible system: a seed, N and the number of row operations.
The sets start as single valves in random order, then a random set gets
another one added (as a symmetric difference) the given number of times,
which keeps the sets independent. Valves in a list come in random order."""

import random
import sys


def main():
    seed, n, ops = (int(x) for x in sys.argv[1:4])
    rng = random.Random(seed)
    valves = list(range(n))
    rng.shuffle(valves)
    rows = [1 << v for v in valves]
    for _ in range(ops):
        i, j = rng.sample(range(n), 2) if n > 1 else (0, 0)
        if i != j:
            rows[i] ^= rows[j]
    lines = [str(n)]
    for r in rows:
        items = [v + 1 for v in range(n) if r >> v & 1]
        rng.shuffle(items)
        lines.append(" ".join(map(str, items + [-1])))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
