"""Checker: as many flags as expected, each a nonempty set of colors from
1 to n, every two flags with a common color and no color on three or
more flags."""

import sys
from itertools import combinations

MOST_FLAGS = 2  # a color may appear on at most this many flags


class Bad(Exception):
    pass


def check(source, expected, output):
    n = int(open(source).read().split()[0])
    want = int(open(expected).read().split()[0])
    words = [int(w) for w in open(output).read().split()]
    if not words or words[0] != want:
        raise Bad("expected %d flags" % want)
    pos, flags = 1, []
    for _ in range(want):
        if pos >= len(words):
            raise Bad("too few numbers")
        size = words[pos]
        flag = words[pos + 1:pos + 1 + size]
        pos += 1 + size
        if size < 1 or len(flag) != size or len(set(flag)) != size:
            raise Bad("a flag needs distinct colors")
        if not all(1 <= c <= n for c in flag):
            raise Bad("a color is out of range")
        flags.append(set(flag))
    if pos != len(words):
        raise Bad("extra output")
    uses = {}
    for flag in flags:
        for c in flag:
            uses[c] = uses.get(c, 0) + 1
            if uses[c] > MOST_FLAGS:
                raise Bad("color %d is on three flags" % c)
    for a, b in combinations(range(want), 2):
        if not flags[a] & flags[b]:
            raise Bad("flags %d and %d share no color" % (a + 1, b + 1))


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
