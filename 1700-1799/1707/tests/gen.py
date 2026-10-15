"""One test from a seed and a mode: mode 1 small n with short and long
experiments, mode 2 the largest sizes, mode 3 the largest counts on a
small grid, mode 4 the largest sizes with few and slow laws, so that the
answers mix zeros and ones. Mode 5 repeats one boundary point at the largest
law counts, mode 6 fills one row with overlapping laws at the largest counts,
and mode 7 uses one point with the largest query count and random moving
prefixes and suffixes on alternating axes."""

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


def structured(rng, mode):
    n = MOST_N
    if mode == 5:
        laws = [(n - 1, 0, 0, 0, MOST_K)] * MOST_M
    elif mode == 6:
        laws = [(5 * i % n, n // 2, 1, 0, MOST_K) for i in range(MOST_M)]
    else:
        laws = [(rng.randrange(1, n - 1), rng.randrange(1, n - 1), 0, 0, 1)]
    print(n, len(laws))
    for law in laws:
        print(*law)
    print(MOST_P)
    for i in range(MOST_P):
        if mode == 5:
            if i % 4 == 0:
                corners, deltas = [n - 1, n - 1, 0, 0], [0, 0, 0, 0]
            elif i % 4 == 1:
                corners, deltas = [n - 2, n - 2, 0, 0], [0, 0, 0, 0]
            elif i % 4 == 2:
                corners = [n - 1, rng.randrange(n), 0, 0]
                deltas = [0, step(rng, n, False), 0, 0]
            else:
                corners = [n - 1, n - 1, 0, rng.randrange(n)]
                deltas = [0, 0, step(rng, n, False), step(rng, n, False)]
        elif mode == 6:
            y = n // 2 - i % MOST_Q
            corners = [rng.randrange(n), rng.randrange(n), y, y]
            deltas = [step(rng, n, False), step(rng, n, False), 1, 1]
        else:
            moving = rng.randrange(n)
            fixed = 0 if i % 4 < 2 else n - 1
            delta = step(rng, n, False)
            if i % 2 == 0:
                corners, deltas = [fixed, moving, 0, n - 1], [0, delta, 0, 0]
            else:
                corners, deltas = [0, n - 1, fixed, moving], [0, 0, 0, delta]
        print(*(corners + deltas + [MOST_Q]))


def main():
    seed, mode = (int(x) for x in sys.argv[1:3])
    rng = random.Random(seed)
    if mode in (5, 6, 7):
        structured(rng, mode)
        return
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
