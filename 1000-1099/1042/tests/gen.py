"""Modes: SEED N OPS for a random invertible system; offdiag N for even N.

The offdiag mode gives every technician every valve except their own; for
even N these sets are independent and all technicians are needed.
In random mode the sets start as single valves in random order, then a random set gets
another one added (as a symmetric difference) the given number of times,
which keeps the sets independent. Valves in a list come in random order."""

import random
import sys


def main():
    if sys.argv[1] == "offdiag":
        n = int(sys.argv[2])
        if not 2 <= n <= 250 or n % 2:
            raise SystemExit("offdiag requires even N between 2 and 250")
        print(n)
        for t in range(1, n + 1):
            print(*(v for v in range(1, n + 1) if v != t), -1)
        return
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
