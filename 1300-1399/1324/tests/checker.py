"""Checker: the output gives the same, minimal number of replacements and
then a plan whose reach is the largest possible, the same as for the
expected plan, and at least L. The reach of a plan is the longest K such
that every run of 1 to K spaces ends up as a single space."""

import sys


def reach(plan):
    """Going back from the last replacement: a step that replaces k spaces
    by one turns every run of up to (M + 3 - k) k - 2 spaces into a run of
    at most M spaces, if 2 <= k <= M + 1, and gains nothing otherwise."""
    longest = 1
    for k in reversed(plan):
        if 2 <= k <= longest + 1:
            longest = (longest + 3 - k) * k - 2
    return longest


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, ans, output = sys.argv[1:4]
    limit = int(open(inp).read().split()[0])
    expected = [int(x) for x in open(ans).read().split()]
    got = open(output).read().split()
    if not got or not all(x.isdigit() for x in got):
        fail("expected whole numbers")
    got = [int(x) for x in got]
    if got[0] != expected[0]:
        fail("%d replacements, the minimum is %d" % (got[0], expected[0]))
    if len(got) != got[0] + 1:
        fail("expected %d lengths" % got[0])
    if 0 in got[1:]:
        fail("a replacement of 0 spaces")
    best, mine = reach(expected[1:]), reach(got[1:])
    if mine < limit:
        fail("the plan leaves a run of %d spaces" % (mine + 1))
    if mine != best:
        fail("the plan handles runs up to %d, the best handles %d" % (mine, best))


if __name__ == "__main__":
    main()
