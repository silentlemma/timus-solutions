"""Deterministic railway input modes:

SEED N L3 TOP: random lengths L1 < L2 < L3, prices C1 < C2 < C3 <= TOP,
neighbouring gaps at most L3, and two distinct random query stations.
dense N: 2 <= N <= 10000 stations spaced 100000 apart, all reachable with
one cheapest ticket; query the first and last stations.
"""

import random
import sys


def main():
    if sys.argv[1] == "dense":
        n = int(sys.argv[2])
        if not 2 <= n <= 10000:
            raise SystemExit("dense requires 2 <= N <= 10000")
        print("999900000 999999999 1000000000 2 3 4")
        print(n)
        print(1, n)
        for i in range(1, n):
            print(i * 100000)
        return

    seed, n, l3, top = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    l1, l2 = sorted(rng.sample(range(1, l3), 2))
    c1, c2, c3 = sorted(rng.sample(range(1, top + 1), 3))
    position, positions = 0, []
    for _ in range(n - 1):
        position += rng.randint(1, l3)
        positions.append(position)
    a, b = rng.sample(range(1, n + 1), 2)
    lines = ["%d %d %d %d %d %d" % (l1, l2, l3, c1, c2, c3), str(n), "%d %d" % (a, b)]
    print("\n".join(lines + [str(p) for p in positions]))


if __name__ == "__main__":
    main()
