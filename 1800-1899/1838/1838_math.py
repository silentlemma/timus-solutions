import sys


def main():
    data = list(map(int, sys.stdin.read().split()))
    length, n = data[0], data[1]
    s = data[2:2 + n]
    # a cut at x between supports s[i] and s[i + 1] leaves both parts
    # standing when the left centre x/2 lies in [s[0], s[i]] and the right
    # centre (x + length)/2 lies in [s[i + 1], s[-1]]
    lo_all, hi_all = 2 * s[0], 2 * s[-1] - length
    safe = 0
    for a, b in zip(s, s[1:]):
        lo = max(a, lo_all, 2 * b - length)
        hi = min(b, hi_all, 2 * a)
        safe += max(0, hi - lo)
    print(length - safe)


main()
