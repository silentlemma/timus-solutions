import sys


def main():
    s = sys.stdin.readline().strip()
    n = len(s)
    best_start, best_len = 0, 0
    # every letter and every gap between two letters is a centre, 2n - 1 in all, and
    # each is expanded as far as it goes; ties keep the leftmost start
    for centre in range(2 * n - 1):
        lo, hi = centre // 2, (centre + 1) // 2
        while lo >= 0 and hi < n and s[lo] == s[hi]:
            lo -= 1
            hi += 1
        length, start = hi - lo - 1, lo + 1
        if length > best_len or (length == best_len and start < best_start):
            best_start, best_len = start, length
    print(s[best_start : best_start + best_len])


main()
