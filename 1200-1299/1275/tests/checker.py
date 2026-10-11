"""Checker: -1 is right only when the reference prints -1. Otherwise the
number of visits must equal the reference's (the least possible), every
visit must serve two knights K apart around the table, no knight may run
out of goblets when they are carried away, and every knight must end
with F goblets."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, ans, output = sys.argv[1:4]
    data = [int(t) for t in open(inp).read().split()]
    n, k, f = data[:3]
    goblets = data[3 : 3 + n]
    best = int(open(ans).read().split()[0])
    tokens = open(output).read().split()
    if not tokens:
        fail("empty output")
    try:
        m = int(tokens[0])
    except ValueError:
        fail("expected a number of visits")
    if m == -1 or best == -1:
        if m != best:
            fail("printed %d, expected %d" % (m, best))
        return
    if m != best:
        fail("%d visits, the least is %d" % (m, best))
    if len(tokens) != 1 + 3 * m:
        fail("expected %d visits of three tokens" % m)
    for v in range(m):
        a, b, sign = tokens[1 + 3 * v : 4 + 3 * v]
        try:
            a, b = int(a) - 1, int(b) - 1
        except ValueError:
            fail("visit %d: bad knight numbers" % (v + 1))
        if not (0 <= a < n and 0 <= b < n) or (b - a) % n not in (k % n, (n - k) % n):
            fail("visit %d: knights %d and %d are not K apart" % (v + 1, a + 1, b + 1))
        if sign not in "+-" or len(sign) != 1:
            fail("visit %d: the sign must be + or -" % (v + 1))
        step = 1 if sign == "+" else -1
        goblets[a] += step
        goblets[b] += step
        if goblets[a] < 0 or goblets[b] < 0:
            fail("visit %d takes a goblet that is not there" % (v + 1))
    if any(g != f for g in goblets):
        fail("not every knight ends with %d goblets" % f)


if __name__ == "__main__":
    main()
