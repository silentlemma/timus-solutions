"""Deterministic talk inputs.

SEED N TOP LONGEST: random talks (the original mode).
chain SEED N TOP: every pair (1, 2), (3, 4), ... plus random talks,
    shuffled; requires 2 <= TOP <= 30000 and TOP // 2 <= N <= 100000.
"""

import random
import sys


def main():
    if sys.argv[1] == "chain":
        seed, n, top = map(int, sys.argv[2:])
        assert 2 <= top <= 30000 and top // 2 <= n <= 100000
        rng = random.Random(seed)
        talks = [(s, s + 1) for s in range(1, top, 2)]
        while len(talks) < n:
            s = rng.randint(1, top - 1)
            talks.append((s, rng.randint(s + 1, top)))
        rng.shuffle(talks)
        sys.stdout.write(str(n) + "\n")
        sys.stdout.write("".join("%d %d\n" % talk for talk in talks))
        return

    seed, n, top, longest = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    lines = [str(n)]
    for _ in range(n):
        s = rng.randint(1, top - 1)
        lines.append("%d %d" % (s, min(top, s + rng.randint(1, longest))))
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
