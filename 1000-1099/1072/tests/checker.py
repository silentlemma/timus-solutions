"""Checker: No when the expected answer is No; otherwise Yes and a path
from the first computer to the second, with as many computers as the
expected path, where every two neighbours share a subnet."""

import sys

BYTE = 256


def address(s):
    value = 0
    for part in s.split("."):
        value = value * BYTE + int(part)
    return value


def read_network(path):
    tok = open(path).read().split()
    n = int(tok[0])
    pos = 1
    nets = []
    for _ in range(n):
        k = int(tok[pos])
        pos += 1
        own = set()
        for _ in range(k):
            own.add(address(tok[pos]) & address(tok[pos + 1]))
            pos += 2
        nets.append(own)
    return n, nets, int(tok[pos]), int(tok[pos + 1])


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, expected, output = sys.argv[1:4]
    n, nets, start, end = read_network(inp)
    want = open(expected).read().split()
    got = open(output).read().split()
    if want[0] == "No":
        if got != ["No"]:
            fail("expected No")
        return
    if not got or got[0] != "Yes":
        fail("expected Yes")
    try:
        path = [int(x) for x in got[1:]]
    except ValueError:
        fail("non-integer token")
    if len(path) != len(want) - 1:
        fail("the path has %d computers, the shortest has %d" % (len(path), len(want) - 1))
    if path[0] != start or path[-1] != end:
        fail("the path does not go from %d to %d" % (start, end))
    for a, b in zip(path, path[1:]):
        if not (1 <= a <= n and 1 <= b <= n) or not (nets[a - 1] & nets[b - 1]):
            fail("computers %d and %d share no subnet" % (a, b))


main()
