"""A random railway; a seed, N, L3 and the largest price. L1 < L2 < L3 and
C1 < C2 < C3 are random, neighbouring stations are at most L3 apart and the
two stations are random (in any order)."""

import random
import sys


def main():
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
