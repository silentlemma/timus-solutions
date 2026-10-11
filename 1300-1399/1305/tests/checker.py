"""Checker: the hull is unique, but the walk around it may start at any
vertex, so the output must be the expected list of vertices turned round
to some starting point, still counterclockwise."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def vertices(path):
    words = open(path).read().split()
    if len(words) % 2:
        fail("an odd number of coordinates")
    return [(int(words[i]), int(words[i + 1])) for i in range(0, len(words), 2)]


def main():
    _, ans, output = sys.argv[1:4]
    expected, got = vertices(ans), vertices(output)
    if len(got) != len(expected):
        fail("%d vertices instead of %d" % (len(got), len(expected)))
    if not got:
        fail("no vertices")
    if got[0] not in expected:
        fail("vertex %d %d is not on the hull" % got[0])
    shift = expected.index(got[0])
    if got != expected[shift:] + expected[:shift]:
        fail("the vertices are not the hull walked counterclockwise")


if __name__ == "__main__":
    main()
