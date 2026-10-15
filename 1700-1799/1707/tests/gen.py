"""One test from a seed and a mode: mode 1 small n with short and long
experiments, mode 2 the largest sizes, mode 3 the largest counts on a
small grid, mode 4 the largest sizes with few and slow laws, so that the
answers mix zeros and ones."""

import random
import sys

MOST_N = 5000
MOST_M = 1000
MOST_K = 567
MOST_P = 345
MOST_Q = 345


def step(rng, n, slow):
    if slow:
        return rng.randint(-2, 2) % n if n > 1 else 0
    return rng.randint(-(n - 1), n - 1)


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode == 1:
        n, m, k_most, p, q_most = rng.randint(1, 12), rng.randint(1, 6), 8, 30, 40
    elif mode == 2:
        n, m, k_most, p, q_most = MOST_N, MOST_M, MOST_K, MOST_P, MOST_Q
    elif mode == 3:
        n, m, k_most, p, q_most = 60, MOST_M, MOST_K, MOST_P, MOST_Q
    else:
        n, m, k_most, p, q_most = MOST_N, 3, MOST_K, MOST_P, MOST_Q
    slow = mode == 4
    lines = [f"{n} {m}"]
    for _ in range(m):
        k = k_most if mode in (2, 3) else rng.randint(1, k_most)
        lines.append(" ".join(map(str, (
            rng.randrange(n), rng.randrange(n), step(rng, n, slow), step(rng, n, slow), k))))
    lines.append(str(p))
    for _ in range(p):
        q = q_most if mode in (2, 3) else rng.choice((rng.randint(1, 20), rng.randint(1, q_most)))
        corners = [rng.randrange(n) for _ in range(4)]
        if slow:
            # thin rectangles: a narrow range of s or of t
            corners[1] = min(n - 1, corners[0] + rng.randint(0, 3))
        deltas = [step(rng, n, False) for _ in range(4)]
        lines.append(" ".join(map(str, corners + deltas + [q])))
    print("\n".join(lines))


main()
