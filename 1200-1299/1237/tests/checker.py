"""Checker: OPTIMAL must match the reference. A SUBOPTIMAL answer must be
followed by an N x M plan of non-negative integers that sends every
worker of each building, stays within every shelter's capacity and has a
smaller total time than the given plan; the reference must agree that the
given plan is not optimal."""

import sys


def fail(message):
    print(message)
    sys.exit(1)


def main():
    inp, ans, output = sys.argv[1:4]
    data = iter(map(int, open(inp).read().split()))
    n, m = next(data), next(data)
    buildings = [(next(data), next(data), next(data)) for _ in range(n)]
    shelters = [(next(data), next(data), next(data)) for _ in range(m)]
    given = [[next(data) for _ in range(m)] for _ in range(n)]
    time = [[abs(x - p) + abs(y - q) + 1 for p, q, _ in shelters] for x, y, _ in buildings]
    want = open(ans).read().split()[0]
    tokens = open(output).read().split()
    if not tokens or tokens[0] not in ("OPTIMAL", "SUBOPTIMAL"):
        fail("the first word must be OPTIMAL or SUBOPTIMAL")
    if tokens[0] != want:
        fail("answered %s, expected %s" % (tokens[0], want))
    if want == "OPTIMAL":
        if len(tokens) != 1:
            fail("extra output after OPTIMAL")
        return
    if len(tokens) != 1 + n * m:
        fail("expected %d numbers in the plan, got %d" % (n * m, len(tokens) - 1))
    try:
        plan = [[int(tokens[1 + i * m + j]) for j in range(m)] for i in range(n)]
    except ValueError:
        fail("the plan holds a non-integer")
    for i in range(n):
        if any(e < 0 for e in plan[i]):
            fail("a negative count in row %d" % (i + 1))
        if sum(plan[i]) != buildings[i][2]:
            fail("building %d sends %d workers, not %d" % (i + 1, sum(plan[i]), buildings[i][2]))
    for j in range(m):
        if sum(plan[i][j] for i in range(n)) > shelters[j][2]:
            fail("shelter %d is over capacity" % (j + 1))

    def total(p):
        return sum(time[i][j] * p[i][j] for i in range(n) for j in range(m))

    if total(plan) >= total(given):
        fail("the plan takes %d, not less than the given %d" % (total(plan), total(given)))


if __name__ == "__main__":
    main()
