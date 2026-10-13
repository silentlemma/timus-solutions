"""Checker: the stated value must be the expected minimum, the table must
hold every number from 1 to N^2 once, and no two neighbouring cells may
sum to more than the stated value, which must also be reached."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, expected, output = sys.argv[1:4]
    n = int(open(inp).read().split()[0])
    want = int(open(expected).read().split()[0])
    try:
        got = [int(x) for x in open(output).read().split()]
    except ValueError:
        fail("not integers")
    if len(got) != 1 + n * n:
        fail("expected the value and %d numbers" % (n * n))
    if got[0] != want:
        fail("the value is %d, expected %d" % (got[0], want))
    table = got[1:]
    if sorted(table) != list(range(1, n * n + 1)):
        fail("the table is not a permutation of 1..N^2")
    worst = 0
    for i in range(n):
        for j in range(n):
            here = table[i * n + j]
            if i + 1 < n:
                worst = max(worst, here + table[(i + 1) * n + j])
            if j + 1 < n:
                worst = max(worst, here + table[i * n + j + 1])
    if worst != got[0]:
        fail("the largest neighbour sum is %d, not %d" % (worst, got[0]))


main()
