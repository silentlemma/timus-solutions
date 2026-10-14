import sys
from math import gcd

FASTEST = 100000  # no speed above this
MOST = 19  # K < 20 leagues
SLACK = 1e-9  # floating point margin for the pruning bound
BIG = 1 << 61


def main():
    m, n = map(int, sys.stdin.read().split())
    # M / N hours over legs of one league each: M / N = 1 / V1 + ... + 1 / VK
    # with distinct whole speeds, a sum of distinct unit fractions
    harmonic = [0.0] * (FASTEST + 2)
    for d in range(1, FASTEST + 1):
        harmonic[d] = harmonic[d - 1] + 1.0 / d

    def most(start, count):
        """The largest sum of count unit fractions with denominators from start."""
        end = min(start + count - 1, FASTEST)
        return harmonic[end] - harmonic[start - 1] if start <= end else 0.0

    path = []

    def search(p, q, last, left):
        """Writes p / q as left or fewer unit fractions above 1 / last."""
        if p == 0:
            return True
        if left == 0:
            return False
        start = max(last + 1, -(-q // p))  # 1 / d must fit into p / q
        # left fractions of 1 / d at most
        stop = FASTEST if q > BIG // left else min(FASTEST, left * q // p)
        if start > stop or most(start, left) + SLACK < p / q:
            return False
        for d in range(start, stop + 1):
            if p / q - 1.0 / d > most(d + 1, left - 1) + SLACK:
                continue
            # keep every fraction within 64 bits
            if q > BIG // d or p > BIG // d:
                continue
            np, nq = p * d - q, q * d
            g = gcd(np, nq)
            path.append(d)
            if search(np // g, nq // g, d, left - 1):
                return True
            path.pop()
        return False

    # the fewest fractions first keeps the search small
    for k in range(1, MOST + 1):
        if search(m, n, 0, k):
            print(len(path))
            print(*reversed(path))
            return
    print(-1)


main()
