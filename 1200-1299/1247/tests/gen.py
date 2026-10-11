"""A sequence: a seed, S, a mode and a target N. Mode 1 draws values 0, 1
and 2 and mode 2 is mostly ones with a few large values and zeros; both
then set N so that the sum is S + N, and nearly always get NO. Mode 3
walks the prefix sums of A_i - 1 inside [0, N] and ends at N, so every
segment sum is at most N and the answer is YES. Mode 4 distributes N + 1
extra units randomly among S - 1 positive values, then appends zero:
the prefix of length S - 1 exceeds its bound by exactly one (NO)."""

import random
import sys

TOP = 100
LIMIT = 30000


def main():
    seed, s, mode, target = (int(x) for x in sys.argv[1:5])
    rng = random.Random(seed)
    if mode == 4:
        if not (2 <= s <= LIMIT and 1 <= target <= LIMIT and target + 1 <= 99 * (s - 1)):
            raise ValueError("mode 4 needs enough capacity for N + 1 extra units")
        a = [1] * (s - 1)
        extra = target + 1
        while extra:
            i = rng.randrange(s - 1)
            delta = min(rng.randint(1, TOP - 1), TOP - a[i], extra)
            a[i] += delta
            extra -= delta
        a.append(0)
    elif mode == 3:
        a, level = [], 0
        for k in range(s):
            left = s - k - 1
            steps = [
                d for d in (-1, 0, 1) if 0 <= level + d <= target and level + d + left >= target
            ]
            d = rng.choice(steps)
            level += d
            a.append(d + 1)
    else:
        if mode == 1:
            a = [rng.randint(0, 2) for _ in range(s)]
        else:
            a = [rng.choice([1] * 20 + [0, 0, TOP, rng.randint(2, TOP)]) for _ in range(s)]
        # nudge the sum into S + 1 .. S + 30000
        while sum(a) - s < 1:
            i = rng.randrange(s)
            a[i] = min(TOP, a[i] + 1)
        while sum(a) - s > LIMIT:
            i = rng.randrange(s)
            a[i] = max(0, a[i] - 1)
    lines = ["%d %d" % (s, sum(a) - s)] + [str(x) for x in a]
    sys.stdout.write("\n".join(lines) + "\n")


if __name__ == "__main__":
    main()
