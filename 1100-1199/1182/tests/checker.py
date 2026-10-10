"""Checker: "No solution" exactly when the stored answer says so; otherwise
two non-empty teams that split everyone, where all members of a team know
each other both ways, and whose sizes differ as little as in the stored
answer."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def teams(tokens):
    # two lines "count id id ..." read as tokens
    k = 0
    out = []
    for _ in range(2):
        size = int(tokens[k])
        out.append([int(t) for t in tokens[k + 1 : k + 1 + size]])
        if len(out[-1]) != size:
            raise ValueError
        k += 1 + size
    if k != len(tokens):
        raise ValueError
    return out


def main():
    inp, ans, output = sys.argv[1:4]
    data = iter(map(int, open(inp).read().split()))
    n = next(data)
    knows = [set() for _ in range(n + 1)]
    for i in range(1, n + 1):
        for j in iter(lambda: next(data), 0):
            knows[i].add(j)
    want = open(ans).read().split()
    got = open(output).read().split()
    if want == ["No", "solution"] or got == ["No", "solution"]:
        if got != want:
            fail("expected %s" % " ".join(want[:2]))
        return
    try:
        first, second = teams(got)
        best = teams(want)
    except (ValueError, IndexError):
        fail("expected two teams")
    if not first or not second or sorted(first + second) != list(range(1, n + 1)):
        fail("the teams do not split everyone into two non-empty groups")
    for team in (first, second):
        for a in team:
            for b in team:
                if a != b and b not in knows[a]:
                    fail("%d does not know %d" % (a, b))
    if abs(len(first) - len(second)) != abs(len(best[0]) - len(best[1])):
        fail("the teams could be closer in size")


if __name__ == "__main__":
    main()
