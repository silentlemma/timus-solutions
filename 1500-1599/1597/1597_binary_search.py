import sys

MOST_DROPS = 2 * 10**9  # two eggs already cover 10^18 floors with this many


def covered(t, k, n):
    """Floors that t drops with k eggs can settle, the sum of C(t, i) over
    i = 1..k, or n + 1 if that is more."""
    total, term = 0, 1
    for i in range(1, k + 1):
        term = term * (t - i + 1) // i
        if term == 0:
            break
        total += term
        if total > n:
            return n + 1
    return total


def drops(k, n):
    if k == 1:
        return n
    lo, hi = 1, MOST_DROPS
    while lo < hi:
        mid = (lo + hi) // 2
        if covered(mid, k, n) >= n:
            hi = mid
        else:
            lo = mid + 1
    return lo


def main():
    words = sys.stdin.read().split()
    out = []
    for i in range(0, len(words) - 1, 2):
        k, n = int(words[i]), int(words[i + 1])
        if k == 0 and n == 0:
            break
        out.append(drops(k, n))
    print("\n".join(map(str, out)))


main()
