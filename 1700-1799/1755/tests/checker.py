"""Checker: the piece must fit in the cake, and after Karlsson takes the
part he likes more (leaving the choice to Little Boy on a tie), Little Boy must
get as much as with the expected piece."""

import sys

TIE = 1e-6
WORTH = 1e-5
ROOM = 1e-7


class Bad(Exception):
    pass


def check(source, expected, output):
    a1, b1, a2, b2, n, m = (int(w) for w in open(source).read().split())

    def boy_gets(x, y):
        mine, rest = a1 * x + b1 * y, a1 * (n - x) + b1 * (m - y)
        his, other = a2 * x + b2 * y, a2 * (n - x) + b2 * (m - y)
        if abs(his - other) <= TIE:
            return max(mine, rest)
        return rest if his > other else mine

    want = [float(w) for w in open(expected).read().split()]
    got = open(output).read().split()
    if len(got) != len(want):
        raise Bad("expected two numbers")
    try:
        x, y = (float(w) for w in got)
    except ValueError:
        raise Bad("the answer is not two numbers")
    if not (-ROOM <= x <= n + ROOM and -ROOM <= y <= m + ROOM):
        raise Bad("the piece does not fit in the cake")
    best, have = boy_gets(*want), boy_gets(x, y)
    if have < best - WORTH:
        raise Bad("Little Boy gets %.8f, but %.8f is possible" % (have, best))


def main():
    try:
        check(*sys.argv[1:4])
    except Bad as e:
        print(e)
        sys.exit(1)


main()
