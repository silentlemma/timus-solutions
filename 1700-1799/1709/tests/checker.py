"""Checker: the printed sum is the least possible, the plan is a
symmetric matrix of 0, d and a with d only on existing flights and a
only on missing ones, the plan's sum matches the printed one, and the
flights after the plan form a spanning tree."""

import sys


class Bad(Exception):
    pass


def check(source, expected, output):
    words = open(source).read().split()
    n, d, a = int(words[0]), int(words[1]), int(words[2])
    flights = words[3:3 + n]
    best = int(open(expected).read().split()[0])
    got = open(output).read().split()
    if len(got) != n + 1:
        raise Bad("expected the sum and %d rows" % n)
    if int(got[0]) != best:
        raise Bad("the sum is %s, the least is %d" % (got[0], best))
    plan = got[1:]
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            x = parent[x]
        return x

    spent = edges = 0
    for i in range(n):
        if len(plan[i]) != n or plan[i][i] != "0":
            raise Bad("row %d is malformed" % (i + 1))
        for j in range(n):
            c = plan[i][j]
            if c not in "0ad" or c != plan[j][i]:
                raise Bad("cell (%d, %d) is wrong or not symmetric" % (i + 1, j + 1))
            if j <= i:
                continue
            exists = flights[i][j] == "1"
            if (c == "d" and not exists) or (c == "a" and exists):
                raise Bad("cell (%d, %d) changes nothing" % (i + 1, j + 1))
            spent += d if c == "d" else a if c == "a" else 0
            if (exists and c != "d") or c == "a":
                edges += 1
                parent[find(i)] = find(j)
    if spent != best:
        raise Bad("the plan costs %d, not %d" % (spent, best))
    if edges != n - 1 or len({find(v) for v in range(n)}) != 1:
        raise Bad("the flights after the plan are not a spanning tree")


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
