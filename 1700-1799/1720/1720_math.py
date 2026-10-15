import sys


def covered(t, x, y):
    # numbers 1 .. t that are sums of contests: k contests give [kx, ky],
    # once k (y - x) >= x - 1 the next interval touches this one, so from
    # the first such k on everything is covered, and before it they are apart
    if t < x:
        return 0
    if y == x:
        return t // x
    joined = max(1, (x - 1 + (y - x) - 1) // (y - x))
    full = min(joined - 1, t // y)  # the intervals that end by t
    count = (y - x) * (full * (full + 1) // 2) + full
    k = full + 1
    if k <= joined - 1 and k <= t // x:
        count += t - k * x + 1
    if joined <= t // x:
        count += t - joined * x + 1
    return count


def main():
    x, y, low, high = (int(w) for w in sys.stdin.read().split())
    print(covered(high, x, y) - covered(low - 1, x, y))


main()
