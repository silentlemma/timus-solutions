"""Checker: the frogs can always swap, so the output must be K and K hummock
numbers, at most a million, each a legal slide or jump into the empty
hummock, ending with the black frogs first and the white frogs last."""

import sys

MOVES = 10**6
EMPTY, WHITE, BLACK = 0, 1, 2


def fail(reason):
    print(reason)
    sys.exit(1)


def main():
    inp, _, output = sys.argv[1:4]
    n = int(open(inp).read().split()[0])
    try:
        got = [int(x) for x in open(output).read().split()]
    except ValueError:
        fail("not integers")
    if not got or got[0] < 0:
        fail("the frogs can always swap")
    k = got[0]
    moves = got[1:]
    if len(moves) != k:
        fail("expected %d moves, got %d" % (k, len(moves)))
    if k > MOVES:
        fail("more than a million moves")
    hummocks = [WHITE] * n + [EMPTY] + [BLACK] * n
    hole = n
    for i, f in enumerate(moves):
        if not 0 <= f <= 2 * n:
            fail("move %d: no hummock %d" % (i + 1, f))
        frog = hummocks[f]
        step = hole - f
        if frog == BLACK:
            ok = step == -1 or (step == -2 and hummocks[f - 1] == WHITE)
        elif frog == WHITE:
            ok = step == 1 or (step == 2 and hummocks[f + 1] == BLACK)
        else:
            ok = False
        if not ok:
            fail("move %d from hummock %d is illegal" % (i + 1, f))
        hummocks[hole], hummocks[f] = frog, EMPTY
        hole = f
    if hummocks != [BLACK] * n + [EMPTY] + [WHITE] * n:
        fail("the frogs have not swapped")


main()
