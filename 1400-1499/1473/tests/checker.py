"""Checker: -1 exactly when the reference says so; otherwise the same
smallest K and K pairs of integers up to 2*10^9 in absolute value, under
which strictly more than half of the experts judge every animal right."""

import sys

LIMIT = 2 * 10**9
CAMEL = 1


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, expected, output = sys.argv[1:4]
    data = [int(x) for x in open(inp).read().split()]
    animals = [tuple(data[1 + 3 * j : 4 + 3 * j]) for j in range(data[0])]
    want = int(open(expected).read().split()[0])
    try:
        got = [int(x) for x in open(output).read().split()]
    except ValueError:
        fail("not integers")
    if not got:
        fail("empty output")
    if want == -1:
        if got != [-1]:
            fail("expected -1")
        return
    if got[0] != want:
        fail("expected %d experts, got %d" % (want, got[0]))
    if len(got) != 1 + 2 * want:
        fail("expected %d pairs" % want)
    experts = [(got[1 + 2 * i], got[2 + 2 * i]) for i in range(want)]
    if any(abs(x) > LIMIT for e in experts for x in e):
        fail("a coefficient is too large")
    for j, (a, b, c) in enumerate(animals):
        sign = 1 if c == CAMEL else -1
        right = sum(1 for x, y in experts if sign * (x * a + y * b) > 0)
        if 2 * right <= want:
            fail("animal %d is judged wrong" % (j + 1))


main()
