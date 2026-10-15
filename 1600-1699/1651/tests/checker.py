"""Checker: accept any shortest walk whose edges occur in input order."""

import sys


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    source, _, output = sys.argv[1:4]
    data = [int(w) for w in open(source).read().split()]
    n = data[0]
    chain = data[1 : n + 1]
    try:
        path = [int(w) for w in open(output).read().split()]
    except ValueError:
        fail("non-integer token")
    if not path or path[0] != chain[0] or path[-1] != chain[-1]:
        fail("wrong endpoints")
    # After each input edge, keep the shortest walk using the scanned prefix.
    best = {chain[0]: 0}
    for a, b in zip(chain, chain[1:]):
        if a in best:
            candidate = best[a] + 1
            if b not in best or candidate < best[b]:
                best[b] = candidate
    if len(path) - 1 != best[chain[-1]]:
        fail("not the minimum number of edges")
    # The earliest matching edge leaves the largest suffix for the rest.
    pos = 0
    for a, b in zip(path, path[1:]):
        while pos < n - 1 and (chain[pos], chain[pos + 1]) != (a, b):
            pos += 1
        if pos == n - 1:
            fail("edges do not occur in input order")
        pos += 1


main()
