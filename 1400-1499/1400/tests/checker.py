"""Checker: the smallest mean with two digits, and the key presses of
every character from one start cursor whose mean is that smallest one."""

import sys


def distances(n, m, start):
    dist = [-1] * n
    dist[start] = 0
    queue = [start]
    for v in queue:
        for u in ((v - 1) % n, (v + 1) % n, v - m if v >= m else v, v + m if v + m < n else v):
            if dist[u] < 0:
                dist[u] = dist[v] + 1
                queue.append(u)
    return dist


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, _, output = sys.argv[1:4]
    n, m = map(int, open(inp).read().split()[:2])
    every = [distances(n, m, s) for s in range(n)]
    least = min(sum(d) for d in every)
    words = open(output).read().split()
    if words[:2] != ["Mean", "="] or len(words) != 3 + n:
        fail("expected Mean = X and %d numbers" % n)
    if words[2] != "%.2f" % (least / n):
        fail("the mean should be %.2f" % (least / n))
    lines = [line.split() for line in open(output).read().splitlines()[1:] if line.strip()]
    if [len(line) for line in lines] != [min(m, n - r) for r in range(0, n, m)]:
        fail("expected %d numbers per line" % m)
    try:
        got = [int(w) for w in words[3:]]
    except ValueError:
        fail("expected integers")
    if not any(got == d and sum(d) == least for d in every):
        fail("the numbers do not come from a best start")


main()
