"""Checker: N integers within 10^9 in absolute value that make the king's
program count exactly (N * N + 3 * N - 4) / 2 steps, by running its
partition with an explicit stack."""

import sys

LIMIT = 10**9


def fail(reason):
    print(reason)
    sys.exit(1)


def steps(a):
    total = 0
    stack = [(0, len(a) - 1)]
    while stack:
        lo, hi = stack.pop()
        if lo >= hi:
            continue
        x = a[lo]
        i, j = lo - 1, hi + 1
        while True:
            j -= 1
            total += 1
            while a[j] > x:
                j -= 1
                total += 1
            i += 1
            total += 1
            while a[i] < x:
                i += 1
                total += 1
            if i < j:
                a[i], a[j] = a[j], a[i]
            else:
                break
        stack.append((lo, j))
        stack.append((j + 1, hi))
    return total


def main():
    inp, _, output = sys.argv[1:4]
    n = int(open(inp).read().split()[0])
    try:
        a = [int(x) for x in open(output).read().split()]
    except ValueError:
        fail("non-integer token")
    if len(a) != n:
        fail("expected %d numbers" % n)
    if any(abs(x) > LIMIT for x in a):
        fail("a number is out of range")
    got, want = steps(a), (n * n + 3 * n - 4) // 2
    if got != want:
        fail("the program counts %d steps, not %d" % (got, want))


main()
