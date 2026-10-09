"""Checker: the first number is the smallest sum (as in the expected
answer), then the count and that many dominoes with faces 1..6 whose sum
is that number, and the given dominoes together with them can be laid out
in a chain: the faces in use are connected and at most two have an odd
number of domino halves."""

import sys

FACES = 6


def fail(message):
    print(message)
    sys.exit(1)


def main():
    inp, expected, output = sys.argv[1:4]
    data = list(map(int, open(inp).read().split()))
    n = data[0]
    dominoes = [(data[1 + 2 * k], data[2 + 2 * k]) for k in range(n)]
    best = int(open(expected).read().split()[0])
    try:
        out = list(map(int, open(output).read().split()))
    except ValueError:
        fail("non-integer token")
    if len(out) < 2 or len(out) != 2 + 2 * out[1] or out[1] < 0:
        fail("expected the sum, the count and that many dominoes")
    total, count = out[0], out[1]
    extra = [(out[2 + 2 * k], out[3 + 2 * k]) for k in range(count)]
    if any(not (1 <= v <= FACES) for d in extra for v in d):
        fail("faces must be from 1 to 6")
    if total != sum(a + b for a, b in extra):
        fail("the sum does not match the dominoes")
    if total != best:
        fail("the sum %d is not the smallest %d" % (total, best))
    parent = list(range(FACES + 1))

    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x

    degree = [0] * (FACES + 1)
    for a, b in dominoes + extra:
        degree[a] += 1
        degree[b] += 1
        parent[find(a)] = find(b)
    used = [v for v in range(1, FACES + 1) if degree[v]]
    if len({find(v) for v in used}) > 1:
        fail("the dominoes do not form one connected group")
    if sum(degree[v] % 2 for v in used) > 2:
        fail("more than two faces with an odd count")


main()
