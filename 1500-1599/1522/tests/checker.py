"""Checker: the printed time must equal the expected minimum, and the
order must be a permutation of the toys that finishes in that time."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    source, expected, output = sys.argv[1:4]
    data = list(map(int, open(source).read().split()))
    n = data[0]
    toys = [data[1 + 3 * i : 4 + 3 * i] for i in range(n)]
    want = int(open(expected).read().split()[0])
    try:
        values = [int(v) for v in open(output).read().split()]
    except ValueError:
        fail("not numbers")
    if len(values) != n + 1:
        fail("expected the time and %d toys, got %d numbers" % (n, len(values)))
    if values[0] != want:
        fail("time %d, expected %d" % (values[0], want))
    order = values[1:]
    if sorted(order) != list(range(1, n + 1)):
        fail("the order is not a permutation of 1 ... %d" % n)
    done_a = done_b = done_c = 0
    for i in order:
        a, b, c = toys[i - 1]
        done_a += a
        done_b = max(done_b, done_a) + b
        done_c = max(done_c, done_b) + c
    if done_c != want:
        fail("the order takes %d, expected %d" % (done_c, want))


main()
