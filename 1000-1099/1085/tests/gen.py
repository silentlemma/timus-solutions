"""A random city: a seed, N, M, the longest route, K, the most money
(everyone has at least half of it) and the share of friends with a pass
in percent."""

import random
import sys

PERCENT = 100


def main():
    seed, n, m, longest, k, money, passes = (int(x) for x in sys.argv[1:8])
    rng = random.Random(seed)
    lines = ["%d %d" % (n, m)]
    for _ in range(m):
        size = rng.randint(2, min(longest, n)) if n >= 2 else 2
        stops = (
            [rng.randint(1, n) for _ in range(size)] if n < 2 else rng.sample(range(1, n + 1), size)
        )
        lines.append(" ".join(map(str, [len(stops)] + stops)))
    lines.append(str(k))
    for _ in range(k):
        card = 1 if rng.randrange(PERCENT) < passes else 0
        cash = rng.randint(max(1, money // 2), money)
        lines.append("%d %d %d" % (cash, rng.randint(1, n), card))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
