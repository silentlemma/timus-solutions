"""Checker: -1 exactly when the expected answer is -1; otherwise at most
200 swaps of two different numbers, after which, swapping rows and
columns together, no contest uses a room with a smaller number."""

import sys

MOST_SWAPS = 200


class Bad(Exception):
    pass


def check(source, expected, output):
    words = open(source).read().split()
    n = int(words[0])
    grid = [words[1 + i * n:1 + (i + 1) * n] for i in range(n)]
    want = open(expected).read().split()
    got = open(output).read().split()
    if want == ["-1"]:
        if got != ["-1"]:
            raise Bad("the timetable cannot be mended, expected -1")
        return
    if not got or not all(w.isdigit() for w in got):
        raise Bad("expected whole numbers")
    t = int(got[0])
    if t > MOST_SWAPS or len(got) != 1 + 2 * t:
        raise Bad("expected at most %d swaps, each two numbers" % MOST_SWAPS)
    label = list(range(n))
    for s in range(t):
        i, j = int(got[1 + 2 * s]) - 1, int(got[2 + 2 * s]) - 1
        if not (0 <= i < n and 0 <= j < n) or i == j:
            raise Bad("swap %d is not two different numbers from 1 to %d" % (s + 1, n))
        label[i], label[j] = label[j], label[i]
    for i in range(n):
        for j in range(i):
            if grid[label[i]][label[j]] == "1":
                raise Bad("contest %d still uses room %d" % (i + 1, j + 1))


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
