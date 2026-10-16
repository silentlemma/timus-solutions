"""Checker: -1 exactly when the expected answer is -1; otherwise as many
blades as expected, each a whole blade named once, and the blades left
are not none and balance: their tips sum to zero."""

import math
import sys

LIMIT = 1e-6


class Bad(Exception):
    pass


def check(source, expected, output):
    words = open(source).read().split()
    n, k = int(words[0]), int(words[1])
    broken = {int(w) for w in words[2:2 + k]}
    want = open(expected).read().split()
    got = open(output).read().split()
    if want == ["-1"]:
        if got != ["-1"]:
            raise Bad("the engine cannot be balanced, expected -1")
        return
    if not got or not all(w.lstrip("-").isdigit() for w in got):
        raise Bad("expected whole numbers")
    count, names = int(got[0]), [int(w) for w in got[1:]]
    if count != int(want[0]) or len(names) != count:
        raise Bad("%d blades named, %s needed" % (len(names), want[0]))
    if len(set(names)) != count or not all(1 <= v <= n and v not in broken for v in names):
        raise Bad("the blades must be whole, distinct and between 1 and %d" % n)
    left = set(range(1, n + 1)) - broken - set(names)
    if not left:
        raise Bad("no blades are left")
    x = sum(math.cos(2 * math.pi * v / n) for v in left)
    y = sum(math.sin(2 * math.pi * v / n) for v in left)
    if math.hypot(x, y) > LIMIT:
        raise Bad("the blades left do not balance")


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
