"""Checker: two lines of N problem numbers that together are 1 to 2N, with
no similar pair in the same round; IMPOSSIBLE only when no such split
exists, which is decided here by colouring the conflict graph and a
subset-sum over its components."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def possible(n, pairs):
    total = 2 * n
    near = [[] for _ in range(total + 1)]
    for a, b in pairs:
        near[a].append(b)
        near[b].append(a)
    colour = [-1] * (total + 1)
    sums = {0}
    for start in range(1, total + 1):
        if colour[start] >= 0:
            continue
        colour[start] = 0
        count, queue = [1, 0], [start]
        for v in queue:
            for w in near[v]:
                if colour[w] < 0:
                    colour[w] = 1 - colour[v]
                    count[colour[w]] += 1
                    queue.append(w)
                elif colour[w] == colour[v]:
                    return False
        sums = {s + c for s in sums for c in count}
    return n in sums


def main():
    inp, _, output = sys.argv[1:4]
    tok = list(map(int, open(inp).read().split()))
    n, m = tok[0], tok[1]
    pairs = [(tok[2 + 2 * k], tok[3 + 2 * k]) for k in range(m)]
    lines = [line.split() for line in open(output).read().split("\n") if line.strip()]
    can = possible(n, pairs)
    if lines == [["IMPOSSIBLE"]]:
        if can:
            fail("a split exists")
        return
    if not can:
        fail("expected IMPOSSIBLE")
    if len(lines) != 2 or any(len(line) != n for line in lines):
        fail("expected two lines of %d numbers" % n)
    rounds = [set(map(int, line)) for line in lines]
    if rounds[0] | rounds[1] != set(range(1, 2 * n + 1)) or rounds[0] & rounds[1]:
        fail("the rounds must split the problems 1 to %d" % (2 * n))
    for a, b in pairs:
        if any(a in r and b in r for r in rounds):
            fail("problems %d and %d share a round" % (a, b))


if __name__ == "__main__":
    main()
