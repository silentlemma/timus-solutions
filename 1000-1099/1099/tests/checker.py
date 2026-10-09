"""Checker: the number of scheduled guards must equal the expected one,
which is the size of a maximum matching, and the listed pairs must be
pairs from the input with every guard in at most one of them."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, expected, output = sys.argv[1:4]
    tok = list(map(int, open(inp).read().split()))
    n = tok[0]
    allowed = {(min(a, b), max(a, b)) for a, b in zip(tok[1::2], tok[2::2]) if a != b}
    want = int(open(expected).read().split()[0])
    try:
        got = [int(x) for x in open(output).read().split()]
    except ValueError:
        fail("non-integer token")
    if not got or got[0] != want:
        fail("expected %d scheduled guards" % want)
    if len(got) != 1 + want:
        fail("expected %d pairs" % (want // 2))
    used = set()
    for a, b in zip(got[1::2], got[2::2]):
        if (min(a, b), max(a, b)) not in allowed:
            fail("guards %d and %d cannot work together" % (a, b))
        if a in used or b in used or not (1 <= a <= n and 1 <= b <= n):
            fail("guard %d or %d is scheduled twice" % (a, b))
        used.update((a, b))


main()
