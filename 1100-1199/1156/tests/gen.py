"""Similar pairs among 2N problems: a seed, N, M and a mode. Mode 0 joins
problems across a hidden split into two rounds, mode 1 joins random
problems, mode 2 joins one problem to many others so that one side is too
big, mode 3 builds many stars of different sizes that need the right mix
of sides."""

import random
import sys


def main():
    seed, n, m, mode = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    total = 2 * n
    pairs = []
    if mode == 0:
        order = rng.sample(range(1, total + 1), total)
        left, right = order[:n], order[n:]
        pairs = [(rng.choice(left), rng.choice(right)) for _ in range(m)]
    elif mode == 2:
        hub = rng.randint(1, total)
        others = [v for v in range(1, total + 1) if v != hub]
        pairs = [(hub, v) for v in rng.sample(others, min(m, len(others)))]
    elif mode == 3:
        free = rng.sample(range(1, total + 1), total)
        while free and len(pairs) < m:
            size = rng.randint(1, min(len(free) - 1, 6)) if len(free) > 1 else 0
            if not size:
                break
            hub, leaves = free[0], free[1 : 1 + size]
            pairs += [(hub, v) for v in leaves][: m - len(pairs)]
            free = free[1 + size :]
    else:
        pairs = [tuple(rng.sample(range(1, total + 1), 2)) for _ in range(m)]
    lines = ["%d %d" % (n, len(pairs))] + ["%d %d" % p for p in pairs]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
