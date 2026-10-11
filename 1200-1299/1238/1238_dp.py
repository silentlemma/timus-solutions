import sys


def main():
    s = sys.stdin.read().split()[0]
    n = len(s)
    best = [[0] * n for _ in range(n)]
    cut = [[0] * n for _ in range(n)]  # > 0: split before s[cut]; < 0: -cut is the period
    for size in range(1, n + 1):
        for i in range(n - size + 1):
            j = i + size - 1
            here, how = size, 0
            row = best[i]
            for k in range(i + 1, j + 1):
                length = row[k - 1] + best[k][j]
                if length < here:
                    here, how = length, k
            # a period p repeats when the segment equals itself shifted by p
            for p in range(1, size):
                if size % p == 0 and s[i : j + 1 - p] == s[i + p : j + 1]:
                    length = len(str(size // p)) + 2 + row[i + p - 1]
                    if length < here:
                        here, how = length, -p
            row[j], cut[i][j] = here, how

    def fold(i, j):
        c = cut[i][j]
        if c > 0:
            return fold(i, c - 1) + fold(c, j)
        if c < 0:
            return "%d(%s)" % ((j - i + 1) // -c, fold(i, i - c - 1))
        return s[i : j + 1]

    print(fold(0, n - 1))


main()
