"""Checker: the output must be P, Q and L with L equal to the reference
side, the square [P, P+L] x [Q, Q+L] inside the park and no tree strictly
inside it (trees on its border are allowed)."""

import sys


def fail(message):
    print(message)
    sys.exit(1)


def main():
    inp, ans, output = sys.argv[1:4]
    data = list(map(int, open(inp).read().split()))
    n, w, h = data[:3]
    trees = [(data[3 + 2 * i], data[4 + 2 * i]) for i in range(n)]
    want = int(open(ans).read().split()[2])
    tokens = open(output).read().split()
    if len(tokens) != 3:
        fail("expected three numbers")
    try:
        p, q, side = (int(t) for t in tokens)
    except ValueError:
        fail("not integers")
    if side != want:
        fail("side %d, expected %d" % (side, want))
    if p < 0 or q < 0 or p + side > w or q + side > h:
        fail("the field leaves the park")
    for x, y in trees:
        if p < x < p + side and q < y < q + side:
            fail("tree (%d, %d) is inside the field" % (x, y))


if __name__ == "__main__":
    main()
