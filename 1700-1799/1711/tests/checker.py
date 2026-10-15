"""Checker: IMPOSSIBLE exactly when expected; otherwise n names, the i-th
one offered for the i-th problem of the order, in increasing order."""

import sys

CHOICES = 3
NONE = "IMPOSSIBLE"


class Bad(Exception):
    pass


def check(source, expected, output):
    data = open(source).read().split()
    n = int(data[0])
    names = [set(data[1 + CHOICES * i:1 + CHOICES * (i + 1)]) for i in range(n)]
    order = [int(w) - 1 for w in data[1 + CHOICES * n:1 + (CHOICES + 1) * n]]
    want = open(expected).read().split()
    got = open(output).read().split()
    if want == [NONE] or got == [NONE]:
        if want != got:
            raise Bad("expected %s" % (NONE if want == [NONE] else "a choice of names"))
        return
    if len(got) != n:
        raise Bad("expected %d names" % n)
    for i, name in enumerate(got):
        if name not in names[order[i]]:
            raise Bad("%s is not offered for problem %d" % (name, order[i] + 1))
        if i > 0 and not got[i - 1] < name:
            raise Bad("%s does not come after %s" % (name, got[i - 1]))


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
