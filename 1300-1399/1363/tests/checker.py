"""Checker: N lines of M numbers, each 0 or 255, such that around every
pixel the window of rows and columns within 10, cut at the borders, has
an average difference from the original of at most 20."""

import sys

RADIUS = 10
LIMIT = 20


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, _, output = sys.argv[1:4]
    words = open(inp).read().split()
    n, m = int(words[0]), int(words[1])
    a = [int(w) for w in words[2 : 2 + n * m]]
    got = open(output).read().split()
    if len(got) != n * m:
        fail("expected %d numbers, got %d" % (n * m, len(got)))
    if any(w not in ("0", "255") for w in got):
        fail("every number must be 0 or 255")
    # prefix sums of the difference, one extra row and column of zeros
    pre = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n):
        acc = 0
        for j in range(m):
            acc += int(got[i * m + j]) - a[i * m + j]
            pre[i + 1][j + 1] = pre[i][j + 1] + acc
    for i in range(n):
        top, bottom = max(0, i - RADIUS), min(n, i + RADIUS + 1)
        for j in range(m):
            left, right = max(0, j - RADIUS), min(m, j + RADIUS + 1)
            diff = pre[bottom][right] - pre[top][right] - pre[bottom][left] + pre[top][left]
            if abs(diff) > LIMIT * (bottom - top) * (right - left):
                fail(
                    "the window around (%d, %d) is off by %.2f on average"
                    % (i + 1, j + 1, diff / ((bottom - top) * (right - left)))
                )


if __name__ == "__main__":
    main()
