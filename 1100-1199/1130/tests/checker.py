"""Checker: YES and a line of N signs + or -, and the signed sum of the
vectors no farther from the start than sqrt(2) L, compared exactly as
squared lengths. Such signs always exist, so WRONG ANSWER is rejected."""

import sys

FACTOR = 2


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, _, output = sys.argv[1:4]
    tok = iter(map(int, open(inp).read().split()))
    n, length = next(tok), next(tok)
    vectors = [(next(tok), next(tok)) for _ in range(n)]
    lines = open(output).read().split()
    if not lines or lines[0] != "YES":
        fail("signs always exist, expected YES")
    if len(lines) != 2 or len(lines[1]) != n or set(lines[1]) - set("+-"):
        fail("expected one line of %d signs" % n)
    sx = sy = 0
    for (x, y), c in zip(vectors, lines[1]):
        s = 1 if c == "+" else -1
        sx += s * x
        sy += s * y
    if sx * sx + sy * sy > FACTOR * length * length:
        fail("the walk ends at (%d, %d), farther than sqrt(2) L" % (sx, sy))


if __name__ == "__main__":
    main()
